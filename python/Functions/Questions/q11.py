#WAf to take the 3 numbers from the users and find the sum of the first two and subtract the third number from the result of addition



n1 = int(input("Enter the num1:-->"))
n2 = int(input("Enter the num2:-->"))
n3 = int(input("Enter the num3:-->"))


def numbers(n1,n2,n3):
  res = n1 + n2
  return res - n3

print(numbers(n1,n2,n3))
