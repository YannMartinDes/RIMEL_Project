import glob2
import csv

def findEndIndex(string):
    count=0
    for i in range(len(string)):
        if ((string[i]=='{') or (string[i]=='(')):
            count=count+1
        if ((string[i]=='}') or (string[i]==')')):
            count=count-1
        if (count==0 and string[i]==";"):
            return i
    return None


ListFile=glob2.glob(r".\rapidminer-studio-modular-master\rapidminer-studio-core\src\main\java\com\rapidminer\operator\**/*.java")

def findPrecondition(ListFile):
    count=0
    res = {}

    for File in ListFile:
        file1 = open(File, 'r')
        
        body = file1.read()
        startIndex=body.strip().find(".addPrecondition")
        
        if (startIndex>=0):
            fileName = File.split('\\')[-1]
            res[fileName] = []
            
        while (startIndex >= 0):
            stringToEvaluate=body[startIndex:len(body)]
            endIndex=findEndIndex(stringToEvaluate)
            
            code = body[startIndex:startIndex+endIndex]
            res[fileName].append(code)

            count=count+1
            body=body[startIndex+endIndex:]
            startIndex=body.strip().find(".addPrecondition")
        file1.close()
    return res
        
def overrideDict(listPreCond):
    res = {}

    for key in listPreCond:
        for cond in listPreCond[key]:
            if(cond.find("@Override") >0):
                if(key in res):
                    res[key].append(cond)
                else:
                    res[key] = [cond]
    
    return res   

def preconditionDict(ListFile):
    count=0
    dictList = {}
    for File in ListFile:
        file1 = open(File, 'r')
        body = file1.read()
        startIndex=body.strip().find(".addPrecondition")
        
            
        while (startIndex >= 0):
            override= "Not Overrode"
            stringToEvaluate=body[startIndex:len(body)]
            startNamePrecondition = stringToEvaluate.strip().find("new ")
            if startNamePrecondition<50:
                startIndex+=startNamePrecondition+4
                stringToEvaluate=body[startIndex:len(body)]
                endIndex=findNextParenthesis(stringToEvaluate)
            else:
                endIndex = startIndex+51

            if(endIndex-startIndex<50):
                stringToEvaluate=body[startIndex-(startNamePrecondition+4):len(body)]
                endPreconditionIndex=findEndIndex(stringToEvaluate)
                if body[startIndex-(startNamePrecondition+4):startIndex+endPreconditionIndex].strip().find("@Override")>0:
                    override="Overrode"
                if File in dictList:
                    dictList[File].append([body[startIndex:startIndex+endIndex],override])
                else :
                    dictList[File]=[[body[startIndex:startIndex+endIndex],override]]
            count=count+1
            if(endIndex != None):
                body=body[startIndex+endIndex:]
            else:
                body=body[startIndex:]
            startIndex=body.strip().find(".addPrecondition")
        file1.close()
    print(count)
    printCSV(dictList)

def printCSV(myDict):
    csv_columns = ['fileName']
    for elem in myDict:
        for precondition in myDict[elem]:
            if precondition[0] not in csv_columns:
                csv_columns.append(precondition[0])
    dict_data=[]
    for elem in myDict:
        data = {}
        data[csv_columns[0]]=elem.split('\\')[-1]
        for column in csv_columns[1:]:
            count = 0
            for precondition in myDict[elem]:
                if precondition[0] == column:
                    count+=1
            print(column)
            print(count)
            data[column]=count
            print(data) 
        dict_data.append(data)
    csv_file = "Nombre_Preconditions_par_fichier_java.csv"
    try:
        with open(csv_file, 'w',newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")
    

def findNextParenthesis(string):
    for i in range(len(string)):
        if (string[i]=='('):
            return i
    return None    

def findTextInBracket(string):
    foundFirst = False
    count=0
    for i in range(len(string)):
        if string[i]=='{':
            foundFirst = True
            count=count+1
        elif string[i]=='}':
            count=count-1
        elif count==0 and foundFirst:
            return i
    return None 

def mandatoryDict(listPreCond):
    res = {}

    for key in listPreCond:
        for cond in listPreCond[key]:
            startInd = cond.find("isMandatory")
            if(startInd >0):
                endInd = findTextInBracket(cond[startInd:])
                mandatoryCode = cond[startInd:startInd+endInd]
                if(key in res):
                    res[key].append(mandatoryCode)
                else:
                    res[key] = [mandatoryCode]
    return res  

#preconditionDict(ListFile)
listPredCond = findPrecondition(ListFile)
overridePredCond = overrideDict(listPredCond)
mandatoryPreCond = mandatoryDict(overridePredCond)


for key in mandatoryPreCond:
    print(key+"--------------------------------------------------------")
    for cond in mandatoryPreCond[key]:
        print(cond)
        print("\n")