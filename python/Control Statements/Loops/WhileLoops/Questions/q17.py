#WAP to find the sum of all the numbers from a given range from users which are divisble by 5 and 7 and get
#all of them in a new list

start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

newls = []
i = start
while i <= end:
    if i % 5 == 0  and i % 7 == 0 :
        newls.append(i)
    i+=1
print(newls)
print(sum(newls))
