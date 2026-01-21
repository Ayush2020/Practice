
#Wpa to check that the given string number is a single digit , double digit or tripple digit

str = input("Enter tht number:")

if len(str) == 1:
    print("Single Digit")
elif len(str) == 2:
    print("Two Digits")
elif len(str) == 3:
    print("Three Digit")
else:
    print("Not a Single Digit")

