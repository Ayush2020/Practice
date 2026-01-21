# wap if input is string retunr its length.else if input is list pop element.else if input is tuple reverse else invalid input"

data = eval(input("Enter The Data: "))

if type(data) == str:
    print(len(data))
elif type(data) == list:
    data.pop()
    print(data)
elif type(data) == tuple:
    print(data[::-1])
else:
    print("Invalid")
