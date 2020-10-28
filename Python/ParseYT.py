from Parse import Parse
from Extract import Extract
from ExtractScript import ExtractScript
from ExtractJSON import ExtractJSON

#Parses a YouTube search
class ParseYT(Parse):
    def __init__(self, parameters={}):
        super().__init__('https://www.youtube.com/results?', parameters)

        self.responseContext = self.json.json_response['responseContext']
        self.estimatedResults = self.json.json_response['estimatedResults']
        self.contents = self.json.json_response['contents']
        self.trackingParams = self.json.json_response['trackingParams']
        self.topbar = self.json.json_response['topbar']
        self.adSafetyReason = self.json.json_response['adSafetyReason']
        

class ParseYT_Channel(ParseYT):
    def __init__(self, channel_name='frenchie mcgee', filter_flag = '&sp=EgIQAg%253D%253D'):
        super().__init__( parameters = {'search_query': channel_name + filter_flag} )

        
        

        

    