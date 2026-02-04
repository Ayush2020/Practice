
# Check that a string is pallindrome or not without using slicing and inbuilt functino

strr = input("enter a String: ")
i = 0

while i < len(strr):
    if strr[i] != strr[len(strr) - 1 - 1]:
        print("Not a pallindrome")
        break
    i+=1
else:
    print(" Pallindrome")