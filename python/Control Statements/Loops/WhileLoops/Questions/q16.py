#WAP to print the sum of all numbers present inside the given list first check that its a number

ls = eval(input("enter the list:"))

i = 0
while i < len(ls):
    if type(ls[i]) == int:
        print(ls[i], end=" ")
    i+=1
