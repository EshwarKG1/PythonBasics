print("Enter total number of elements:")
n = int(input())

lst = []

for i in range(n):
    item = int(input("Enter the number:"))
    lst.append(item)
 
print("List before sorting",lst)
 
for i in range(n):
    for j in range(n-1):
        if lst[j]<lst[j+1]:
            lst[j+1],lst[j] = lst[j],lst[j+1]

print("List after sorting",lst)