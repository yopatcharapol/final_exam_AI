file1 = open("MyFile.txt","r")
for txt in file1.readlines():
    print(txt)
file1.close()
