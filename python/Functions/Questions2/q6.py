#WAP to print below
# def func('TRACXN', 1) print RCN


def func(strr, num):
  rev = ""
  for i in range(1, len(strr), num+1):
    rev += strr[i]
  return rev
  
print(func("TRACXN",1))