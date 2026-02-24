
#//? WAP to  find the factorial of all the numbers present in the list


def factorial(x):
  fact = 1
  for i in range(1, x+1):
    fact *= i
  return fact


res = map(factorial, [1,2,3,4,5,6,7,8])
print(list(res))