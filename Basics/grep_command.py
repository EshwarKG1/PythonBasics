grep = input(">>")
grep_list = grep.split()

#print(grp_l)

actual_grep = ["grep","-c","-o","-v"]
file_n = ["myFile.txt","example.txt"]

count = 0

# -c : We can find the number of lines that matches the given string/pattern
if (grep_list[0] == actual_grep[0]) and (grep_list[1] == actual_grep[1]) and (len(grep_list)==4):
    find_word = grep_list[2].strip('"')# Storing the word to be searched
    if grep_list[3] in file_n: # checking if file exists
        with open(grep_list[3],"r") as file:
            for line in file:
                for word in line.split():
                    if word == find_word:# checking for the word
                        count += 1
                        break
                # print(count)
        if count == 0:
            print("Word not found")
        else:
            print(count)
    else:
        print("File doesnot exists") 
 

# -o : We can make the grep to display only the matched string by using the -o option.   
elif (grep_list[0] == actual_grep[0]) and (grep_list[1] == actual_grep[2]) and (len(grep_list)==4):
    find_word = grep_list[2].strip('"')# Storing the word to be searched
    if grep_list[3] in file_n: # checking if file exists
        with open(grep_list[3],"r") as file:
            for line in file:
                for word in line.split():
                    if word == find_word:# checking for the word
                        print(word) # printing the word
                        count = 1
        if count == 0:
            print("Word not found")
    else:
        print("File doesnot exists") 
  

# -v : You can display the lines that are not matched with the specified search string pattern using the -v option.    
elif (grep_list[0] == actual_grep[0]) and (grep_list[1] == actual_grep[3]) and (len(grep_list)==4):
    find_word = grep_list[2].strip('"')# Storing the word to be searched
    if grep_list[3] in file_n: # checking if file exists
        with open(grep_list[3],"r") as file:
            for line in file:
                myCount = 0
                for word in line.split():
                    if word == find_word:# checking for the word
                        # print(word) # printing the word
                        # count = 1
                        myCount = 1
                if myCount == 0:
                    print(line)
    else:
        print("File doesnot exists") 
        
else:
    print("formate is not correct")