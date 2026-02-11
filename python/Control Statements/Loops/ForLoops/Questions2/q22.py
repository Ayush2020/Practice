#WAP to create a dictionary of word and its reverse pair from a given string 
s = "tomorrow is a weekent"

dictt = {}
s = s.split()

for i in s:
  if i not in dictt:
    dictt[i] = i[::-1]

print(dictt)