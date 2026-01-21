#WAP to check a age belongs to whcih category 0 to 17 child and 18 to 30 ur adult 31 to 60 ur men 61 to 100 senior citiaen
# else invalid


age = int(input("Enter the Age:"))

if age < 0 :
    print("Not an valid age")
elif age > 0 and age <= 17:
    print("Child")
elif age >= 18 and age <= 30:
    print("Adult")
elif age >= 31 and age <= 60:
    print("Men")
elif age >= 61 and age <= 100:
    print("Senior Citizen")
else:
    print("Invalid")
