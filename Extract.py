# +
# #!pip install tabula.py

import tabula
import pandas as pd

def extract(url, prefix, pages='all'):
    '''
    Extracts tables from a PDF at a given link and stores them as CSVs in the Data Folder.
    Example call: extract("<URL>", "001", 12)
    
    Parameters:
        - url (str): URL to extract tables from.
        
        - prefix (str): Tagging number used in Data Folder and Data Bibliography. 
            Examples: '001', '013'
            
        - pages (str, int, iterable of int, optional): An optional values specifying pages to extract from. 
          It allows str,`int`, iterable of :int. Default: 1
            Examples: '1-2, 3', 'all', [1,2]
    '''
    print("Scanning URL...")
    try:
        table = tabula.read_pdf(url, pages=pages, silent=True)
        print("Scan Complete.")
    except Exception as e:
        table = []
        print("Error: No Tables Found.")
    
    if len(table) > 0:
        for i in range(len(table)):
            print("Saving Tables to Data/Raw_Data...\t{}/{}".format(i+1, len(table)))
            name_str = prefix + '.' + str(i+1)
            table[i].to_csv(f'./Data/Raw_Data/{name_str}.csv')

        print("Saving Tables Complete.")
