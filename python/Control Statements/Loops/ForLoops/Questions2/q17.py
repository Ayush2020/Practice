#WAP to count all the occurences of all the characters present inside the given string

s = "character"
dictt = {}

for c in s:
    if c not in dictt:
        dictt[c] =1
    else:
        dictt[c] += 1
print(dictt)