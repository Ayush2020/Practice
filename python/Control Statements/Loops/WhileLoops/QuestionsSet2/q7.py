# Armsstrong number or not  153 = 1^3 + 5^3 + 3^3 = 153 

num = int(input("Enter a number: "))

temp = num
summ = 0

while temp >0:
    digit = temp % 10
    power = digit**3
    summ += power
    temp = temp // 10

if summ == num :
    print("Armstring")
else:
    print("Not Armstring")
