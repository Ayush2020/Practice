
#Nested If


age = int(input("Enter your age: "))
gender = input("Enter the gender: ")

if age >= 18:
    if gender.lower() == "male":
        print("u r Elligible ")
    elif gender.lower() == "female":
        print("u r Elligible miss")
    else:
        print("u r Not Elligible")
else:
    loc = input("Enter your location: ")
    if loc.lower() == "gurgaon":
        print("Milenege fir ")
    else:
        print("nhi Milenege fir ")