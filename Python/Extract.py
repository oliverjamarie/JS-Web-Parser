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

        for i in self.bs.find_all(tag):
            txt = '\n' +  str(i)
            txt += '\n'
            li.append(txt)
        
        return li

