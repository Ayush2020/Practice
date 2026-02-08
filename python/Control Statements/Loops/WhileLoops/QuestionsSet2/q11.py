#Spy number or not 123 --> 1 + 2  + 3 --> 6  and == 1*2*3 = 6 check


num = int(input("Enter the number: "))
summ = 0
product = 1

while num > 0:
    digit = num % 10
    summ += digit
    product *= digit
    num //= 10

# print("\n\n")
print(summ)
print(product)

if summ == product:
    print("Spy Number")
else:
    print("Not an Spy number")