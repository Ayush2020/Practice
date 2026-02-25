
#//! WAP to fetch the numbers from a list whose last digit is 5 or 0

print(list(filter(lambda x : x % 10 == 5 or x % 10 ==0, eval(input("Enter the list---")))))