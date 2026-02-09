#WAP to count the aplhabets and numbers and space in the given string

s = "india got the independence in the year 1947"
s = s.lower()
alpha = 0
num = 0
space = 0

for i in range(len(s)):
    if s[i] == " ":
        space += 1
    elif 'a' <= s[i] <= 'z':
        alpha += 1
    elif '0' <= s[i] <= '9':
        num += 1

print("Count Alpha: ", alpha)
print("Count Number: ", num)
print("Count Space: ", space)