#WAP to check the number is neon means  square of 9  -> 9 * 9 = 81 and 8 + 1 = 9


num = int(input("Enter a number: "))
square = num ** 2
summ = 0
i = 0
while square > 0:
    digit = square % 10
    summ += digit
    square = square // 10

if summ == num:
    print("Neaon")
else:
    print("not neon")