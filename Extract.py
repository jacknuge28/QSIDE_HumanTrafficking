# +
# #!pip install tabula.py

import tabula
import pandas as pd

def extract(url, pages, prefix):
    '''
    Extracts tables from a PDF at a given link and stores them as CSVs in the Data Folder.
    Example call: extract("<URL>", 12, "001")
    
    Parameters:
        - url (str): URL to extract tables from.
        
        - pages (str, int, iterable of int, optional): An optional values specifying pages to extract from. 
          It allows str,`int`, iterable of :int. Default: 1
            Examples: '1-2, 3', 'all', [1,2]
        
        - prefix (str): Tagging number used in Data Folder and Data Bibliography. 
            Examples: '001', '013'
    '''
    print("Scanning URL...")
    table = tabula.read_pdf(url, pages=pages)
    
    for i in range(len(table)):
        print("Saving Tables to Data/Raw_Data...\t{}/{}".format(i+1, len(table)))
        name_str = prefix + '.' + str(i+1)
        table[i].to_csv(f'./Data/Raw_Data/{name_str}.csv')
        
    print("Saving Tables Complete.")
