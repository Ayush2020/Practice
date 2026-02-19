#WAP to count the number of uppercase characters in the given string


strr = "StrInGisInUpPerCaSe"

def func(strr):
  count = 0
  for i in strr:
    if 'A' <= i <= 'Z':
      count +=1
  return count

print(func(strr))