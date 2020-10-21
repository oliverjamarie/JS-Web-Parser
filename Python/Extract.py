import requests
import json
from bs4 import BeautifulSoup


class Extract:
    #   url ==> url of the webpage
    #   flag ==> 
    #       string appended to end of url
    #       used to determine type of query
    #   parameters ==> dictionary used to conduct query

    def __init__(self, url: str, parameters:dict):
        webpage = requests.get(url, params=parameters)
        
        if webpage.status_code != 200:
            raise Exception('Something went wrong. Check the URL')

        self.bs = BeautifulSoup(webpage.content, features='html.parser')

    def get_from_tag(self, tag:str):
        li = []
        tag_length = len(tag)

        for i in self.bs.find_all(tag):
            txt = str(i)
            txt = txt[tag_length + 2:- (tag_length + 3)]
            li.append(txt)
        
        return li

class ExtractScript(Extract):
    def __init__(self, url: str, parameters:dict):
        Extract.__init__(self, url, parameters)
        self.scripts = []

        self.scripts = Extract.get_from_tag(self, 'script')

class ExtractJSON(ExtractScript): 
    def __init__ (self, url: str, parameters:dict):
        ExtractScript.__init__(self,url, parameters)
        self.json_response = {}
        self.json_list = [] 
        self.__get_json()

    def get_attributes(self):
        attributes = []

        for i in self.json_response:
            attributes.append(i)
        
        return attributes

    def save_to_file(self, filename='JSON Response.json'):
        formatted_json_string = self.__format_json_string()

        f = open(filename,'w')
        f.write(formatted_json_string)
        f.close()

    def __format_json_string(self):
        formatted_json_string = ''
        base_string = json.dumps(self.json_response)


        list_str = base_string.split(', ')

        for line in list_str:
            
            formatted_json_string += line + ',\n'    

        formatted_json_string = formatted_json_string[0:-2] #removes the comma at the end

        return formatted_json_string

    def __partition_scripts(self):
        arr = []

        for script in self.scripts:
            li = self.__partition_script(script)
            for item in li:
                arr.append(item)

        return arr
    
    def __partition_script(self,script:str):
        partitioned = []
        string = script[:]

        while string.count('{') > 0:
            part = string.partition('{')
            msg = part[1]
            string = part[2]
            part = string.partition('}')
            msg += part[0] + part[1]
            string = part[2]
            partitioned.append(msg)
    
        return partitioned
        
    def __get_json(self):
        list_scripts = self.__partition_scripts()

        for item in list_scripts:
            if len(item) > 2: #if len(part) < 2, we know it's empty
                try:
                    obj = json.loads(item) 
                    self.json_list.append(obj)
                    self.json_response.update(obj) #adds obj to json_response
                except: #nothing happens if if we get an exception
                    pass 
