

age = int(input("Enter the age: "))
gender = input("Enter your gender: ")

if age >= 18 and gender.lower() == "male":
    print("You are eligible to vote")

if age < 18:
    print("Not eligible to vote")

print("Hello")