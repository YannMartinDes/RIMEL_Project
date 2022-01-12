import glob2
ListFile=glob2.glob(r".\rapidminer-studio-modular-master\rapidminer-studio-core\src\main\java\com\rapidminer\operator\**/*.java")
def finish(string):
    count=0
    for i in range(len(string)):
        if ((string[i]=='{') or (string[i]=='(')):
            count=count+1
        if ((string[i]=='}') or (string[i]==')')):
            count=count-1
        if (count==0 and string[i]==";"):
            return i
    return -1
count=0
for File in ListFile:
    file1 = open(File, 'r')
    line = file1.read()
    while (line.strip().find("addPrecondition") >= 0):
        print(File)
        startIndex=line.strip().find("addPrecondition")
        endString=line[startIndex:len(line)]
        endIndex=finish(endString)
        print(line[startIndex:startIndex+endIndex])
        count=count+1
        line=line[startIndex+endIndex+1:len(line)]       
    file1.close()
print(count)
