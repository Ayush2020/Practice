# Check that a string is pallindrome or not without using slicing and inbuilt functino


strr = input("enter the string:")

i = len(strr) - 1
rev =""

while i >= 0:
    rev += strr[i]
    i-=1

print(rev)
if strr == rev :
    print("pallindrome")
else:
    print("Not ")
