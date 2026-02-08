#WAP to print the table of a number like 2 * i = 2 take this number  from user

num = int(input("Enter a number: "))

i = 1
while i <= num:
    print(f"2 * {i} = {2 * i}")
    i+=1