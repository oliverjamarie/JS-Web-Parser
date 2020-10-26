# Web-Parser

Main purpose of the project is to parse webpages and extract information.
Project can be used for every website but the project is built for specific websites and querys.  
These are the parser's specialisations. 

Data is parsed and stored into the **Extract** object and its child objects.
**Extract** child objects:
  - **ExtractScript** 
    Extracts all the scripts from an html page
  - **ExtractJSON**
    Child of **ExtractScript** 
    Extracts all the json from an html page

Extracted data is analysed in **Parse** object.
Specialisations are child objects of **Parse**.

Current specialisations are:
  - **ParseYT** 
    Does a YouTube search query
  - **ParseYT_Channel** 
    Child object of **ParseYT**
    Extracts channel information from a search query

# Output Files
Whenever you want to save the output, the output would be saved to the **Output Files** directory. 

# Dependencies
 - BeautifulSoup4
 - request standard module 
