import glob2
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

    for File in ListFile:
        file1 = open(File, 'r')
        body = file1.read()
        startIndex=body.strip().find(".addPrecondition")
        
        if (startIndex>=0):
            print(File)
            
        while (startIndex >= 0):
            stringToEvaluate=body[startIndex:len(body)]
            endIndex=findEndIndex(stringToEvaluate)
            
            print(body[startIndex:startIndex+endIndex]+"\n\n")
            count=count+1
            body=body[startIndex+endIndex:]
            startIndex=body.strip().find(".addPrecondition")
        file1.close()
        
    print(count)

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
    print(dictList)

def findNextParenthesis(string):
    count=0
    for i in range(len(string)):
        if (string[i]=='('):
            return i
    return None    

preconditionDict(ListFile)
#findPrecondition(ListFile)
