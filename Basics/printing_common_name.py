f = open("list1.txt","r")
lst1 = f.read()
f.close()

str1 = lst1.split(",")
print(str1)


f = open("list2.txt","r")
lst2 = f.read()
f.close()

str2 = lst2.split(",")
print(str2)
i=0
flag = 0
str3=[]

# if the list is sorted 
"""
while (i<len(str1)) and (j<len(str2)):
    if str1[i] in str2[j]:
        str3.append(str1[i])
        i = i+1
        j = j+1
        count = 1
    elif str1[i] > str2[j]:
        j = j+1
    else:
        i = i+1
 """
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] in str2[j]:
            str3.append(str1[i])
            flag = 1
            break
 
if flag == 1:
    print(str3)
else:
    print("match not found")