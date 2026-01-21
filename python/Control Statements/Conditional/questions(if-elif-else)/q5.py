
#WAP TO check that the given data is of which individual datattype

data = eval(input("Enter a number: "))
if type(data) == int:
    print("Int type")
elif type(data) == float:
    print("Float type")
elif type(data) == complex:
    print("complex type")
elif type(data) == bool:
    print("bool type")
else:
    print("Collctions type")