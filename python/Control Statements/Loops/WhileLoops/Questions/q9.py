#WAP to print all the even positional characters of a given string

strr = input("enter the String : ")

i = 0
while i < len(strr):
    if i % 2 == 0:
        print(strr[i], end=" ")
    i+=1
