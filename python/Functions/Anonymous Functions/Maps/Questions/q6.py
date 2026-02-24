
#//? WAP to find the square of all the values present inside a given range


var = lambda x: x**2 

res = map(var,(i for i in range(int(input("Enter the range: -->")))))
print(list(res))
