#WAP to create a dictionary and print the characters and its ASCiI value pair
s = "hello world"

dictt = {}

for i in range(len(s)):
    if s[i] not in dictt:
        dictt[s[i]] = ord(s[i])

print(dictt)









