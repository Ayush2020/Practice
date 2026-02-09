#WAp to extract vowels and digits from a given strist



strr = input("Enter the string: ")

vowels = ""
digit = ""

for i in range(0, len(strr)):
  if strr[i] in "aeiouAEIOU":
    vowels += strr[i]
  elif strr[i] in "0123456789":
    digit += strr[i]

print("Vowels:", vowels)
print("Digits:", digit)