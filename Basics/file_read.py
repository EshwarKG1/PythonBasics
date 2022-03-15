with open("myFile.txt","r") as file:
    var = file.read()

flag = 0

key = input("Enter the value to replace:")

if key in var:
    key1 = input("Enter value :")
    ans = var.replace(key,key1)
    with open("myFile.txt","w") as file:
        file.write(ans)
    flag = 1
else:
    print("Key not found")
