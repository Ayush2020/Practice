#Write a program to reverse of a number without using slicing or typecasting no inbuilt functions

num = int(input("Enter a number: "))

i = 0
reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10
    i+=1
print(reverse_num)
