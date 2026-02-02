#wap to print the square and square root of all the numbers from a list giiven by user and first check the value is int


n = eval(input("Enter the number"))
i = 0
while(i < len(n)):
  if type(i) == int:
    print(f"The square of {n[i]} is {n[i]**2} and the square root is {n[i]**0.5}")
  i+=1
