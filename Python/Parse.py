import urllib
from urllib.parse import urlparse
import urllib3
import requests
import json
from bs4 import BeautifulSoup

#parses a Youtube search query

list_json = []
scripts = []

def main ():
    filter_flag = '&sp=EgIQAg%253D%253D' #add this to end of the url to only get channels in the query
    parameters = {'search_query': 'frenchie mcgee'+filter_flag}

    webpage = requests.get('https://www.youtube.com/results?', params=parameters)

    print (webpage.url)

    print (webpage.status_code)

    bs = BeautifulSoup(webpage.content, features='html.parser')

    scripts = __get_from_tag(bs,'script')
    list_json = __get_json_list(scripts)

    
def __get_from_tag(bs:BeautifulSoup,tag:str):
    list_scripts = []
    for i in bs.find_all(tag):
        msg = str(i)
        msg = msg[8:-9] #remove the start and end tags
        list_scripts.append(msg)
    return list_scripts

def __partition_script(script:str):
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

def __get_json_list (scripts:list):
    json_list = []
    partitioned = []
    
    for script in scripts:
        arr = __partition_script(script)
        for part in arr:
            partitioned.append(part)
    
    
    for part in partitioned:
        try:
            obj = json.loads(part)
            json_list.append(obj)
        except:
            pass
        
    return json_list

if __name__ == "__main__":
    main()