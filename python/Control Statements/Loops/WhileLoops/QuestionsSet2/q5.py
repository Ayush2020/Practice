#Check is the number is pallindrome or not


num = int(input("Enter the number"))
rev_num = 0
temp = num

while temp > 0:
  digit = temp % 10
  rev_num = rev_num * 10 + digit
  temp //= 10

if rev_num == num :
  print("pallindrome")
else:
  print("not a Palindrome")