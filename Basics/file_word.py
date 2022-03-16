with open("dict.txt","r") as file:
    ele = file.read()
key = ele.split(",")

with open("myWord.txt","r") as f:
    for line in f:
        for word in line.split():
            if word in key:
                pass
            else:
                print(word,"is not present in the dict file")
                flag = int(input("Select 1 for Ignore\nSelect 2 for add\n: "))
                if flag == 2:
                    with open("dict.txt","a") as f:
                        f.write(",")
                        f.write(word)
                    print(word,"successfully added to dict file\n")
                elif flag == 1:
                    print(word,"has been ignored\n")

"""

for i in range(len(words)):
    if words[i] in key:
        #print(words[i]," is present")
        pass
    else:
        print(words[i]," is not present")
        print("Select 1 to ignore")
        print("Select 2 to add")
        flag = int(input())
        if flag == 2:
            with open("dict.txt","a") as f:
                f.write(",")
                f.write(words[i])
        elif flag == 1:
            print(words[i],"has been ignored")

"""

"""
if key in word:
    print("Word is present")
    print(word)
else:
    print(key," is not present")
    flag=int(input("enter one to add:"))
    
if flag == 1:
    f = open("dict.txt","a")
    f.write(" ")
    f.write(key)
    f.close()
"""
