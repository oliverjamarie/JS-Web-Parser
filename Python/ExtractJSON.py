from Extract import Extract
from ExtractScript import ExtractScript
import json
import re

class ExtractJSON(ExtractScript):
    def __init__(self, url: str, parameters:dict):
        ExtractScript.__init__(self,url,parameters)

        self.json_response = {}
        self.get_json()
        self.invalid_json_list = []


    #works using regular expressions based off the assumption that valid json sections start off with 
    # ' {"' 
    # and end with
    # "}  \d}   or ]}
    # it's public so you can call it but the results are always stored in self.json_response 
    def get_json(self):
        self.json_response = {}

        # Potential Patterns
        # r'(\{\"){1}.*(\"\})'
        # r'(\{\")?.*(\"\})'
        # r'\{\"[\w]+\":.*\}'
        pattern = r'\{\"[\w]+\":(.*|\d*|\])\}'
        self.invalid_json_list = []

        for script in self.scripts:

            matches = re.finditer(pattern,script)

            for match in matches:
                start = match.span()[0]
                end = match.span()[1]

                try:
                    obj = json.loads(script[start : end])
                    self.json_response.update(obj)
                except:
                    self.invalid_json_list.append(script[start: end])

    # saves the valid json to "Python/Output Files/Extracted JSON.json"
    # AND
    # saves the invalid json to "Python/Output Files/Extracted Invalid JSON.txt"
    def save_to_file(self):
        with open('Python/Output Files/Extracted JSON.json','w') as f:
            f.write(json.dumps(self.json_response, indent=1, separators=(',',':')))

        with open('Python/Output Files/Extracted Invalid JSON.txt','w') as f:
            if len(self.invalid_json_list) == 0:
                f.write('EMPTY.  NO INVALID JSON')
            else:
                for i in self.invalid_json_list:
                    f.write(i)