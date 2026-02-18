#Check that the number is a perfect number or not 
#6 factors = 1, 2, 3 --> 1+2+3 = 6


num = int(input("Enter the Number--> "))
ls = []


def strong_num(num):
  i = 1
  summ = 0
  while i < num:
    if num % i == 0:
      ls.append(i)
      summ += i
    i+=1
    
  
  if summ == num:
    return "Perfect Number", ls
  else:
    return "Not"
  
print(strong_num(num))