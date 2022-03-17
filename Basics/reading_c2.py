with open("myC1.c","r") as file:
    n_lines = file.readlines()
# print(n_lines)

fo=[]
fc={}
line_count = 0
flag = 0

for i in n_lines:
    # print(i,end='')
    line_count += 1
    if i.startswith('//'): # Checking for the comments and ignoring it 
        pass
    else: # Checking for outside comment statements
        for a in i:
            if '{' in a: # If open bracket found append to list
                fo.append(line_count)
            elif '}' in a: # If close bracket found 
                try:
                    fc[fo.pop()] = line_count # append it to dict with list as the key
                except IndexError: # printing if any close bracket has no open bracket with specifying the line number
                    print("There is no matching opening brackets at",line_count)

if len(fo) > 0 : # printing if any open bracket has no close bracket with specifying the line number
    for i in fo:
        print("There is no matching closing brackets at ",i)