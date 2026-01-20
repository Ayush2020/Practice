#WAP to find  the greatest of two number

num1 = int(input("Enter the Number 1:"))
num2 = int(input("Enter the Number 2:"))

if num1 > num2:
    print("Number 1 is greater than Number 2", num1)
if num2 > num1:
    print("number 2 is greater than number 1", num2)
else:
    print("Both are equal")