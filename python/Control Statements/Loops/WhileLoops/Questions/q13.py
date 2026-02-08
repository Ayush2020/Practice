#wap to print the data from  a list only its of collection datatype

data = eval(input("Enter the input: "))

i = 0
while i < len(data):
    if type(data[i]) in [str, tuple, dict, set, list]:
        print(data[i], end=" ")
    i+=1
