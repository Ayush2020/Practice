# wap to check that the last character of the given string is  a vowel or no t



str =  input("Enter the String : ")

if str[-1].lower() in ["a", "e", "i", "o", "u"]:
    print("Vowel")
else:
    print("Not a Vowel")