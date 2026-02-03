#WAP to print all the names from the list and their first character should be capital and rest of them should be like
#that only with capitalize ad without capitalize

# ls = ['vaidehi', 'rahul', 'shivam']

#With Capitalize
# l = []
# i = 0
# while i < len(ls):
#     if ls[i] != ls[i].capitalize():
#         upper = ls[i].capitalize()
#         l.append(upper)
#     i+=1
# print(l)


#Without Capitalize
ls = ['vaidehi', 'rahul', 'shivam']

l = []
i = 0
while i < len(ls):
  if 97 <= ord(ls[i][0]) <= 122:
    l.append(chr(ord(ls[i][0]) -32) + ls[i][1:])
  else:
    l.append(chr(ord(ls[i][0])) + ls[i][1:])
  i += 1
print(l)