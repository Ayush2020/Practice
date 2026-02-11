#WAP to print the even positional characters from a given string using for loop

s = "characters"

for i in range(2,len(s)):
    if i % 2 == 0:
        print(s[i])

