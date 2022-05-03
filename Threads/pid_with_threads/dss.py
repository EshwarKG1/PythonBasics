def LoadcallbackA():
    a_values = []
    dire = "/home/acufore/Eshwar/New/pid_with_threads/log_files/detectA.JOB"
    with open(dire,"r") as file:
        data = file.readlines()
        values_i = 1
        for k in data:
            #print(k)
            l = k.split(",")
            if values_i == 1:
                l.pop(0)
                values_i = 2
            elif l[0] == '\n':
                l.remove('\n')
            else:
                a_values.append(l[0])       
    return a_values
a = LoadcallbackA()
print(a)