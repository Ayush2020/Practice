# WAP to take marks of 5 subs calculate the average if the average is btw 90 -100 print distintion
#if 75-89 first class and 60-74 second class if 50-59  third class 50  belor fail

sub1 = int(input("Enter a number 1:"))
sub2 = int(input("Enter a number 2:"))
sub3 = int(input("Enter a number 3:"))
sub4 = int(input("Enter a number 4:"))
sub5 = int(input("Enter a number 5:"))

avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

if avg >= 90 and avg <= 100:
    print("Distintion")
elif avg >= 75 and avg <= 89:
    print("First Class")
elif avg >= 60 and avg <= 74:
    print("Second Class")
elif avg >= 50 and avg <= 59:
    print("Third Class")
else:
    print("Fail")

