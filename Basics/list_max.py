# lst = [2,3,4,5]

# n = len(lst)

print("Enter total number of elements:")
n = int(input())

lst = []

for i in range(n):
    item = int(input("Enter the number:"))
    lst.append(item)
    
if n>0:
    maxnum = lst[0]
    for i in range(n):
        if lst[i]>maxnum:
            maxnum = lst[i]
    
    print(lst)
    print(maxnum)

else :
    print("Enter the valid number")

