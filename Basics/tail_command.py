tail = input(">>")
tail_list = tail.split()

#print(tal_l)

actual_tail = ["tail","-n","-v"]
file_n = ["myFile.txt","example.txt"]


# -n : Prints the last ‘n’ lines 
if (tail_list[0] == actual_tail[0]) and (tail_list[1] == actual_tail[1]) and (len(tail_list)==4):
    n = int(tail_list[2]) # Storing the number of lines to print in variable
    if tail_list[3] in file_n:
        with open(tail_list[3],"r") as file:
            for line in (file.readlines() [-n:]):
                print(line,end='')
    else:
        print("File doesnot exists")
   
   
# -v : By using this option, data from the specified file is always preceded by its file name        
elif (tail_list[0] == actual_tail[0]) and (tail_list[1] == actual_tail[2]) and (len(tail_list)==3):
    # n = int(tail_list[2]) # Storing the number of lines to print in variable
    if tail_list[2] in file_n:
        with open(tail_list[2],"r") as file:
            print("==>",tail_list[2],"<==")
            for line in file:
                print(line,end='')
    else:
        print("File doesnot exists")         
else:
    print("formate is not correct")