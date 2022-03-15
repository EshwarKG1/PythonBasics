n = int(input("Enter total number of elements: "))

lst = []

for i in range(n):
    item = input("Enter the element: ")
    lst.append(item)

count = 0

key = input("Enter key value to be replaced: ")

if key in lst:
    key1 = input("Enter the value in replaced position: ")
    count = 1
else:
    print("Key is not present in the list")

print("elements present: ",lst)

if count == 1:
    for i in range(n):
        if lst[i] == key:
            lst[i] = key1
    print("elements present after replace: ",lst)