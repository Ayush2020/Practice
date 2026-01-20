# wap to check that the first character of the given string is a consoant or not

str =  input("Enter the String : ")

if str[0].lower() in ["a", "e", "i", "o", "u"]:
    print("Not an Conssonant")
else:
    print("Conssonant")