import json

with open('./RapidMiner.sikuli/json_data.json') as json_file:
    data = json.load(json_file)

with open('./dictGraph.json') as json_file:
    dictGraphUnfilter = json.load(json_file)


#print(data["Linear Regression"])
uniqueDict={}
for elem in dictGraphUnfilter:
  for op in dictGraphUnfilter[elem]:
    uniqueDict[op]=[]
  

for elem in uniqueDict:
  if (elem in dictGraphUnfilter):
    continue
  
  else :
    dictGraphUnfilter[elem]=[]

dictGraph=dictGraphUnfilter

merged_data = {}
for keyGraph in dictGraph.keys():
    normalizedKey=keyGraph.lower().replace(" ", "")
    for key in data:
        normalizedSecondKey=key.lower().replace(" ", "")
        if normalizedSecondKey == normalizedKey:
            merged_data[keyGraph]=data[key]

#print(merged_data)

with open('mergedDict.json', 'w') as convert_file:
     convert_file.write(json.dumps(merged_data))