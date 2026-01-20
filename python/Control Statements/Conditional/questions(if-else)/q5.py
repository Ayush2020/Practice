#Wap to check the given numbers is even or odd if odd add 1 to that and make it even else find the square of that

num = int(input("Enter a Number: "))

if num % 2 != 0:
    print(num + 1)
else:
    print(num * num)