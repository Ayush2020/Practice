#WAP to print he even indexes and values of a given list  taken from user

l = eval(input("Enter the List: --> "))

for i in range(2,len(l)):
    if i % 2 == 0:
        print(f"Index: {i} value:{l[i]}")

print(l)