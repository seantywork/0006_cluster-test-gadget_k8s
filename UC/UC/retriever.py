import pandas as pd
import re
from pathlib import Path
import os
import hashlib

def retriever(z,clf):
    BASE_DIR = Path(__file__).resolve().parent
    entrypath = os.path.join(BASE_DIR, 'entrydb.csv')
    textpath = os.path.join(BASE_DIR, 'textdb.csv')
    entrydb = pd.read_csv(entrypath)
    textdb = pd.read_csv(textpath)



    result = list()
    match_total_count = 0


    if clf == 1:
        for query in z:
            touched = 0
            for i in range(len(entrydb)):
                #check = re.search('\\b'+query+'\\b',entrydb.at[i,'ENTRY'],flags= re.I)
                if str(query).casefold() == str(entrydb.at[i,'ENTRY']).casefold():
                    if entrydb.at[i,'COUNT'] >= 1 :
                        idxs = str(entrydb.at[i,'INDEX']).split(',')
                        idxslist = [int(x) for x in idxs]
                        match_total_count += 1
                        touched = 1
                        for j in idxslist :
                            result.append([query,textdb.at[j,'USAGE'],entrydb.at[i,'COUNT']])
                    else :
                        touched = 1
                        result.append([query,'No Usage',0])

            if touched == 0:
                result.append([query,'No Entry',0])

            touched = 0



    result_df = pd.DataFrame(result,columns=['ENTRY','USAGE','COUNT'])

    return result_df