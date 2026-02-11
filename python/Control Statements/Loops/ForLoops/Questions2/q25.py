#WAP to create a dictionary with words and its length pair for a given string 
s = "hello good morning how r u"

dict = {}

for i in s.split():
  if i not in dict:
    dict[i] = len(i)

print(dict)