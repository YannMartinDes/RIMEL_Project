


from parserUtils import ListFiles, createDirForResultIfNotExist, findEndIndex, writeDictFile


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


def run():
    listPreCond = findPrecondition(ListFiles)
    createDirForResultIfNotExist("./generate")
    writeDictFile(listPreCond,"./generate/errorResult.txt")

if __name__ == "__main__":
    run()