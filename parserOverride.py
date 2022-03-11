from parserPrecondition import findPrecondition
from parserUtils import ListFiles, createDirForResultIfNotExist, writeDictFile


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

def run():
    listPreCond = findPrecondition(ListFiles)
    overridePreCond = overrideDict(listPreCond)
    createDirForResultIfNotExist("./generate")
    writeDictFile(overridePreCond,"./generate/overridePreCond.txt")

if __name__ == "__main__":
    run()