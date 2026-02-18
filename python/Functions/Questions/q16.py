#WAP to print all the names from a list and their first character should be capital and rest of them should be like that only without built in function only
ls = ['vaidehi', 'rahul', 'shivam']

for i in ls:
  if 'a' <= i[0] <= 'z':
    print(chr(ord(i[0]) - 32) + i[1::])
  


