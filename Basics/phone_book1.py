print("Select anyone option below")
char = int(input(" 1. Add a new member\n 2. Modify a member\n 3. Search a member\n 4. Delete a member\n -> "))

# Adding a new member to phone Book 
if char == 1:
    nam = input("Enter the name: ")
    with open("book.txt","a") as file:
        file.write(nam)
        file.write(",")
    eid  = input("Enter the employee ID: ")
    with open("book.txt","a") as file:
        file.write(eid)
        file.write(",")
    a  = int(input("Enter the Age of employee: "))
    age = str(a)
    with open("book.txt","a") as file:
        file.write(age)
        file.write(",")  
    ph = int(input("Enter the moblie number: "))
    ph_s = str(ph)
    with open("book.txt","a") as file:
        file.write(ph_s)
        file.write(",")
    em = input("Enter the email of employee: ")
    with open("book.txt","a") as file:
        file.write(em)
        file.write("\n")
    print("Successfully added")
  
# Modify a existing Name by the user  
elif char == 2:
    empty=''
    flag_2 = 0
    mod_2 = input("Enter name to modify: ")
    with open("book.txt","r") as file:
        data = file.readlines()
    for i in data:
        if mod_2 in i:
            flag_2 = 1 
    if flag_2 == 1:
        for i in data:
            if i.startswith(mod_2):
                mod_2_1 = input("Enter new name : ")
                i = i.replace(mod_2,mod_2_1)
                empty = empty + i
            else:
                empty = empty + i
                
        with open("book.txt","w") as file:
            file.write(empty)
    else:
        print("name not found")

# Displaying the Name asked by the user(Search)       
elif char == 3:
    flag = 0
    mod_3 = input("Enter name to search: ")
    with open("book.txt","r") as file:
        data_3 = file.readlines()
    for i in data_3:
        if i.startswith(mod_3):
            print(i)
            flag = 1
            break
    if flag == 0:
        print("Name not found")    
 
# Deleting the name specified by the user 
elif char == 4:
    mod_4 = input("Enter name to delete: ")
    with open("book.txt","r") as file:
        data_4 = file.readlines()
    with open("book1.txt","a") as file:
        for line in data_4:
            if line.startswith(mod_4):
                pass
            else:
                file.write(line)
    with open("book1.txt","r") as file:
        data_4_1 = file.read()
    with open("book.txt","w") as file:
        file.write(data_4_1)
        
# If mis-option is typed
else:
    print("Enter the correct option")