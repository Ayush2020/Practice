#WAP to print all the names from a list and their first character should be capital and rest of them should be like that only without built in function only
ls = ['vaidehi', 'rahul', 'shivam']
newls = []


def capital(ls):
  for i in ls:
    if 'a' <= i[0] <= 'z':
      a = chr(ord(i[0]) - 32) + i[1::]
      newls.append(a)
  return newls
  
print(capital(ls))
