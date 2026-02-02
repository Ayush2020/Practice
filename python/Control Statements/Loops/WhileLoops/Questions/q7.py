#wap to find the factorial of a number given by user

n = int(input("enter the number"))

i = 0
fact = 1
while(i<n):
  fact = fact * (n - i)
  i+=1
print(fact)