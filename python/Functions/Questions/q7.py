# check that eh number is strong number or not 


def is_strong(num):
  temp = num
  summ = 0
  while temp > 0:
    i = 1
    digit = temp % 10
    fact = 1
    while i <= digit:
      fact *= i
      i+=1
    summ += fact
    temp//=10
    
    
  if summ == num:
    return "Strong"
  else:
    return "Not Strong"




print(is_strong(145))