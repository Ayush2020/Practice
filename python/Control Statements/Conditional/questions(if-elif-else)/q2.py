#wap to check data is a collection /individual datatype

data = eval(input("Enter the Data: "))

if type(data) in [int, complex, bool, float]:
    print(type(data),"data is of Individaual DataType")
elif type(data) in [str, tuple, set, dict, list]:
    print(type(data), "Data is of Collection Datatype")
else:
    print("Not a Data type")