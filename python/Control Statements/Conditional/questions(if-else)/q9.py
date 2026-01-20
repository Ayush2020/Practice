#wap to check that the data is of individual datatype or collection datataype


data = eval(input("Enter the Data: "))

if type(data) in [int, float, complex, bool]:
    print("Data is Individual Data Type")
else:
    print("data is Collection Data Type")
