#Strong number
# 145 1! + 4! + 5!  = 145  For loop

num = int(input("Enter a number: "))

summ = 0

for i in str(num):
  fact = 1
  for j in range(1, int(i) + 1):
    fact *= j
  summ += fact


if summ == num:
  print("Strong")
else:
  print("not Strong")
