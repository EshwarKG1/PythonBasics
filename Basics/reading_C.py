with open("myC.c","r") as file:
    n_lines = file.readlines()
# print(n_lines)

fo=[]
fc={}
line_count = 0
flag = 0

for i in n_lines:
    # print(i,end='')
    line_count += 1
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

# All the tired code is below .. 
"""
for i in n_lines:
    # print(i,end='')
    line_count += 1
    for a in i:
        if '{' in a:
            fo.append(line_count)
            
        elif '}' in a:
            if len(fo) == 0:
                raise IndexError("No matching closing brackets at:",line_count)
            fc[fo.pop()] = line_count
    if len(fo) > 0:
        raise IndexError("No matching opening brackets at:",line_count)
print(fo)
print(fc)    
"""
"""
i = 0
j = 0

while (i<len(fo)) and (j<len(fc)):
    if fo[i]<fc[j]:
        i += 1
        j += 1
        print(i,j,"fine")
    elif fo[i] == fc[j]:
        i += 1
        j += 1
        print(i,j,"fine")
    else:
        print("Open bracket is not Closed")
        break
if i<(len(fo)):
    for t in range(i,len(fo)):
        print("Open bracket at line",fo[t],"has no close bracket")
if j<(len(fc)):
    for t in range(j,len(fc)):
    print("Close bracket at line",fc[t],"has no open bracket")
"""
"""
        if a == '{':
            print("1")
            print(line_count)
            flag = 1
            print(flag)
        if a == '}':
            print("2")
            print(line_count)
            flag = 0
            print(flag)
        # print(a)
"""



"""
line_count=0
fo = []
fc = []

with open("myC.c","r") as file:
    for line in file:
        line_count += 1
        for word in line.split():
            if word == '{':
                for 
"""
             
# print(file_count)
# print(fo)
# print(fc)

"""
if len(fo) == len(fc):
    print("Fine")
elif len(fo) > len(fc):
    for i in range(len(fc),len(fo)):
        print("Open brack at Line",fo[i],"has no close bracket")
else:
    for i in range(len(fo),len(fc)):
        print("close brack at Line",fc[i],"has no open bracket")
"""