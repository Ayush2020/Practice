#Wap to check thtta the string is starting with upper case or not if not convert the whole string to uppercase else to lower case

str = input("Enter the String : ")

if str[0] != str[0].upper():
    print(str.upper())
else:
    print(str.lower())