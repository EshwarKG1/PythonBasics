var = input("Enter the word:")

ans = ""

for i in var:
    ans = i + ans

if ans == var:
    print("it is palindrome")
else:
    print("not a palindrome")
