
# WAP to fetch only even factorial from a collections from a normal list of range given by user 


def fact(x):
  fact = 1
  for i in range(1,x+1):
    fact*=i
  return fact

print(list(filter(lambda x : x % 2 == 0, map(fact, eval(input("Enter the list---"))))))