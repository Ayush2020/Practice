#Wap to print  all prime number between a particuar range with while loop

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

num = start
while num <= end:
    if num > 1:
        i = 2
        while i < num:
            if (num % i) == 0:
                break
            i += 1
        else:
            print(num)
    num += 1
 