#WAP to check the char is uppercsae or lowercase or digit or special character(using inbuild fucntion)

char = eval(input("Enter the char"))

if char.isupper():
    print("upper case")
elif char.islower():
    print("lower case")
elif char.isdigit():
    print("Digit")
else:
    print("Special")
