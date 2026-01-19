#wap to chekc that given number is divisible by 2 and 5 both if yes than convert it to complex

num =  int(input("Enter the number"))

if num % 2 == 0 and num % 5 == 0:
    a = complex(num)
    print(a)