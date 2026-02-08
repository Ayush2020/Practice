# Check that a string is pallindrome or not without using slicing and inbuilt functino


strr = input("Enter a string: ")

i = len(strr) - 1
rev = ""

while i >= 0:
  rev += strr[i]
  i -=1
if strr == rev:
  print("Pallindrome")
else:
  print("not a pallindrome")
  
print(rev)