#WAp to segregate the values fro 1 - 50 into even and odd number into list

start = int(input("Enter the starting: "))
end = int(input("Enter the ending: "))

odd = []
even = []

for i in range(start, end + 1):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Odd",odd)
print("Even",even)