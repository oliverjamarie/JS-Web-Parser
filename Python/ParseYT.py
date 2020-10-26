from Parse import Parse
from Extract import Extract
from ExtractScript import ExtractScript
from ExtractJSON import ExtractJSON

#Parses a YouTube search
class ParseYT(Parse):
    def __init__(self, parameters={}):
        super().__init__('https://www.youtube.com/results?', parameters)
        self.json = ExtractJSON(self.url, self.parameters)
        self.scripts = ExtractScript(self.url, self.parameters)

class ParseYT_Channel(ParseYT):
    def __init__(self, channel_name='frenchie mcgee', filter_flag = '&sp=EgIQAg%253D%253D'):
        super().__init__( parameters = {'search_query': channel_name + filter_flag} )

        """ self.json = ExtractJSON__OLD(self.url, self.parameters)
        
        self.json_response = self.json.json_response
        self.scripts = self.json.scripts[:] """

        

    