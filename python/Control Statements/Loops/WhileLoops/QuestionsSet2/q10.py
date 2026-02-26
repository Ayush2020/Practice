#--> sum of 1st and last digit == toh the sum of median digits
# 1234 -> 1 + 4 == 5 and 2 + 3 --> 5




num = input("Enter a number: ")

left = 0
right = len(num) - 1

first_last_sum = int(num[left]) + int(num[right])
middle_sum = 0

left += 1
right -= 1

while left < right:
    middle_sum += int(num[left]) + int(num[right])
    left += 1
    right -= 1


if left == right:
    middle_sum += int(num[left])

if first_last_sum == middle_sum:
    print("Equal")
else:
    print("Not Equal")

        