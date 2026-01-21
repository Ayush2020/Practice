#WAP to give hike to an employee based onn his experinece  exp 0 to 2 years no hike and 3 to 5 years 5000rs and 6 - 8  yrs 7000rs
#9 to n yrs 10000rs


exp = int(input("Enter the exp:"))

if exp > 0 and exp <= 2:
    print("No Hike")
elif exp >= 3 and exp <= 5:
    print("5000 Rs Hike")
elif exp >= 6 and exp <= 8:
    print("7000 rs Hike")
elif exp >= 9:
    print("10000 rs Hike")
else:
    print("Nothing")