#WAP to chheck that a number is a strong number or not 
# 145 : 1! + 4! + 5! = 145 

num = int(input("Enter the Number: "))

temp = 0
summ = 0

while temp > 0:
  digit = temp % 10
  fact = 1
  i = 1
  while i<= digit:
    fact *= i
    i+=1
  summ += fact
  temp //= 10

if summ == num:
  print("Strong")
else:
  print("not a Strong")