f = open("myWord.txt","r")
word = f.read()
f.close()

words = word.split(",")

with open("dict.txt","r") as file:
    ele = file.read()

key = ele.split(",")

for i in range(len(words)):
    for j in range(len(key)):
        if words[i] in key[j]:
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