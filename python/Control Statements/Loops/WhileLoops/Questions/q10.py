#WAP  to segregate  even and add numbers between 1 to 100 in two diff even and odd named list


odd = []
even = []
i = 1

while(i <= 100):
    if i % 2 == 0:
        odd.append(i)
    else:
        even.append(i)
    i+=1


print(odd)
print(even)




