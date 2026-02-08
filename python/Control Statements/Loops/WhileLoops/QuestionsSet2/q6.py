#WAP to check th automorphic number or not 5 == 5**2 = 25 alast digit is wqual to actual digit


num = int(input("Enter the number : "))
square = num**2

strr1 = str(num)
strr2 = str(square)

if strr2.endswith(strr1):
    print("Automorphic")
else:
    print("Not Automorphic")