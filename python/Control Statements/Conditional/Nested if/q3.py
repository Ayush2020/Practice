#WAP to validate facebook username and password
#Condition id : ---> username ---> "python" and password = "python masters"

username = input("Enter your username: ")


if username == "python":
    password = input("Enter your password: ")
    if password == "python masters":
        print("Validated User")
    else:
        print("Invalid User")
else:
    print("Wrong Username")