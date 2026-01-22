#WAP to check the number is odd and check if ht number is ivisible by 5 and 7 both  n = 35

num = int(input("Enter the number : "))

if num % 2 != 0:
    if num % 5 == 0:
        if num %  7 == 0 :
            print(num, "is Odd and Divisible by both 5 and 7")
    else:
        print("number cant be divisibele by both 5 and 7")
else:
    print("Number is even")