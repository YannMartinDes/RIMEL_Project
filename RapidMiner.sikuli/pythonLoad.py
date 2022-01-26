# Python program to read
import json
import ast
import pandas as pd
# Opening JSON file
f = open('json_data.json')

# returns JSON object as
# a dictionary
data = f.read()
# Iterating through the json
# list
count=0
dictLocal={}
myDict=json.loads(data)
for elem in myDict:
    if (elem!="DBSCAN"):
        dictLocal[elem]=myDict[elem]
    if(len(myDict[elem])!=0 ):
        count=count+1
# Closing file
print(count)
dataFrame=pd.DataFrame(myDict).T
dataFrame.to_csv('file_name_transpose_yann.csv',encoding = "utf-8",na_rep=None)
print(dataFrame)
f.close()
