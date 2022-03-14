n = int(input("Enter the number:"))

temp = n
sum1 = 0
lst = []
count=0

while temp>0:
    num = temp%10
    lst.append(num)
    temp = temp//10
    count=count+1

for i in range(len(lst)):
    var = lst[i]
    sum1 = sum1 + var**count

if n == sum1:
    print("Armstrong")
else:
    print("Not Armstrong")
