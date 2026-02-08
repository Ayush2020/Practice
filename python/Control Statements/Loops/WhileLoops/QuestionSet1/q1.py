#wap to check that a number is a prime or not 


  
num = int(input("Enter a number: "))
i = 2
is_prime = True
while i < num:
  if num % i == 0:
    is_prime = False
    break
  i+=1
if is_prime:
  print(f"{num} is a prime number")
else:
  print(f"{num} is not a prime number")