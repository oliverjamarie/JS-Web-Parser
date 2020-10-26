from Extract import Extract
import re 

class ExtractScript(Extract):
    def __init__(self, url: str, parameters:dict):
        Extract.__init__(self, url, parameters)
        self.scripts = []

        self.scripts = Extract.get_from_tag(self,'script')

    def save_to_file(self,filename='Exctracted Scripts.html'):
        if filename.endswith('.html') == False:
            raise Exception('Invalid file type.  Use HTML file type')
        with open('Python/Output Files/' + filename,'w') as f:
        
            for script in self.scripts:
                f.write(script)


    
