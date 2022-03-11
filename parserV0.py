# from parserError import additionnalCheckDict, errorDict, mandatoryDict
# from parserOverride import overrideDict
from parserError import additionnalCheckDict, errorDict, mandatoryDict
from parserOverride import overrideDict
from parserPrecondition import findPrecondition
from parserUtils import ListFiles, createDirForResultIfNotExist, writePreconditionDict, writeDictFile








if(__name__=="__main__"):
    listPreCond = findPrecondition(ListFiles)
    overridePreCond = overrideDict(listPreCond)
    mandatoryOverride = mandatoryDict(overridePreCond)
    addCheckOverride = additionnalCheckDict(listPreCond)
    errorAddCheck = errorDict(addCheckOverride)
    createDirForResultIfNotExist("./generate")
    csvContent = writePreconditionDict(ListFiles)
    writeDictFile(listPreCond,"./generate/errorResult.txt")
    writeDictFile(overridePreCond,"./generate/overridePreCond.txt")
    writeDictFile(mandatoryOverride,"./generate/mandatoryOverride.txt")
    writeDictFile(addCheckOverride,"./generate/addCheckOverride.txt")
    writeDictFile(errorAddCheck,"./generate/errorAddCheck.txt")
    # for key in errorAddCheck:
    #     print(key+"--------------------------------------------------------")
    #     for cond in errorAddCheck[key]:
    #         print(cond)
    #         print("\n")