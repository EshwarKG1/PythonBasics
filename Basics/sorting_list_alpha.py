lst = ["banana","apple","mango","aaapple","aapple","maango"]
"""
lst.sort()
print(lst)
"""
n = len(lst)

for i in range(n):
    char = str(lst[i])
    for j in range(i+1,n):
        char1 = str(lst[j])
        if char[0]>char1[0]:
            lst[j],lst[i] = lst[i],lst[j]

for i in range(n):
    char = str(lst[i])
    for j in range(i+1,n):
        char1 = str(lst[j])
        if char[0] == char1[0]:
            if char[1]>char[1]:
                lst[j],lst[i] = lst[i],lst[j]             

for i in range(n):
    char = str(lst[i])
    for j in range(i+1,n):
        char1 = str(lst[j])
        if char[0] == char1[0]:
            if char[1] == char[1]:
                if char[2]>char1[2]:
                    lst[j],lst[i] = lst[i],lst[j]             
print(lst)