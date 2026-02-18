#Check that the number is a xylem number
# 9**2 = 81 --> 8 + 1 --> 9


num = int(input("Enter the num:-->"))

def xylem_num(num):
  square = num**2
  summ = 0

  while square > 0:
    digit = square % 10
    summ += digit
    square //= 10
    
  if summ == num:
    return "Xylem"
  else:
    return "Not a Xylem Number"

print(xylem_num(num))