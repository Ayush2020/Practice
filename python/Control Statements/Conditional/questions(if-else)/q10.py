#wap to check that specified character  is present in the given string or not, take both of them forrom user

char = input("Enter the character to check: ")
str = input("Enter the String : ")

if char in str:
    print("char is present ")
else:
    print("Not present")