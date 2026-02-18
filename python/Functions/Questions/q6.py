#wap to fetch the last digit of a number after performing the addition of two numbers


def last_digit(a, b):
  num = a + b
  temp = num
  digit = temp % 10
  
  return num , digit


print(last_digit(10,25))