import glob2
ListFile=glob2.glob(r"C:\Users\tnersissian\Downloads\rapidminer-studio-modular-master\rapidminer-studio-core\src\main\java\com\rapidminer\operator\**/*.java")
for File in ListFile:
    file1 = open(File, 'r')
    count = 0
    while True:
        count += 1
        line = file1.readline()
        if (line.strip().find("addPrecondition") >= 0):
            print(line.strip())
        if not line:
            break
    file1.close()
print(count)
