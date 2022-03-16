with open("myWord.txt","r") as f:
    word = f.read()

words = word.split(",")

with open("dict.txt","r") as file:
    ele = file.read()

key = ele.split(",")

for i in range(len(words)):
    if words[i] in key:
        print(words[i]," is present")
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
