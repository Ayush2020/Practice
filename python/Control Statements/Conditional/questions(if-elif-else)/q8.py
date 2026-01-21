#WAP to check which is smallest value amoung 3 numbers a = 65 b = 34 c = 76

a = int(input("Enter num a: "))
b = int(input("Enter num b: "))
c = int(input("Enter num c: "))

if a > b and a > c :
    print("a is greater")
elif b > a and b > c :
    print("b is greater")
elif c > a and c > b :
    print("c is greater")
else:
    print("Equal")