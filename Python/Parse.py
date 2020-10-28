
from ExtractJSON import ExtractJSON
from ExtractScript import ExtractScript 

#parses a Youtube search query


class Parse:
    def __init__(self, url='', parameters={}):
        self.parameters = parameters
        self.url = url
        self.json = ExtractJSON(self.url, self.parameters)
        self.scripts = ExtractScript(self.url, self.parameters)






    
