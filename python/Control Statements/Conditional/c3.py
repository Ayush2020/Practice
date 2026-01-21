
#if - ELIF-Else


age = int(input("Enter the Age: "))

if age < 0:
    print("Paida nhi hua h abhi yeh balak")
elif age < 18:
    print("Not Eligible to Vote")
elif age >= 18 and age < 50:
    print("Eligible to vote")
elif age >= 50 and age <= 80:
    print("Tera Samay aane wala h")
elif age > 80 and age <= 100:
    print("niklane wala hi h")
else:
    print("Khtm h seen ")