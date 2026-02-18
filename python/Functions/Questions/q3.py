#WAP to return the square, cube, square root , cube root of a value taken from user

num = int(input("Enter the Number:---> "))

def number(num):
  square = num ** 2
  cube = num ** 3
  sqrt = num **0.5
  cbrt = num **1/3
  return square, cube, sqrt, cbrt


print(number(num))
