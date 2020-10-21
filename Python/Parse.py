
from Extract import * 

#parses a Youtube search query


def main ():
    global filter_flag, parameters, url

    filter_flag = '&sp=EgIQAg%253D%253D' #add this to end of the url to only get channels in the query
    parameters = {'search_query': 'frenchie mcgee'+filter_flag}
    url = 'https://www.youtube.com/results?'


    json = ExtractJSON(url,parameters)
    json.save_to_file()


class Parse:
    def __init__(self, filter_flag='', url='', parameters={}):
        self.filter_flag = filter_flag
        self.parameters = parameters
        self.url = url

#Parses a YouTube search
class ParseYT(Parse):
    def __init__(self, filter_flag='', parameters={}):
        super().__init__(filter_flag, 'https://www.youtube.com/results?', parameters)
        self.json_response = {}
        self.scripts = []

class ParseYT_Channel(ParseYT):
    def __init__(self, channel_name='frenchie mcgee', filter_flag = '&sp=EgIQAg%253D%253D'):
        super().__init__(
            filter_flag, 
            parameters = {'search_query': channel_name + filter_flag})

        self.json = ExtractJSON(self.url, self.parameters)

        self.json_response = self.json.json_response
        self.scripts = self.json.scripts[:]





    
