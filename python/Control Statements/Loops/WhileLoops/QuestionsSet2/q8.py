#Check th e number is perfect number or not 6 find all factors of 6:1 + 2+ 3:1 + 2+ 3 = 6

num = int(input("Enter a number: "))

summ = 0

i = 1
while i <= num//2:
    if num % i == 0:
        print(i, end=" ")
        summ += i
    i+=1



if summ == num:
    print("\nStrong")
else:
    print("Weak")

