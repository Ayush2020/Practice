#WAP to fetch the last digit of a number 

num = int(input("Enter the number--> "))


def last_digit(num):
  digit = num % 10
  return "last digit of a num ",digit
  
print(last_digit(num))