#WAP to check string is pallindrome or not


str =  input("Enter the String : ")

if str == str[::-1]:
    print("String is pallindrome ")
else:
    print("String is not pallindrome")