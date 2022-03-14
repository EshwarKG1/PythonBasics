a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

print("Values before swapping:-")
print("First value:",a)
print("Second value:",b)

'''
var = a
a = b
b = var
'''

a,b = b,a


print("Values after swapping:-")
print("First value:",a)
print("Second value:",b)