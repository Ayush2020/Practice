#WAP to find the number of same bits of same length strings
#s1 = '010101010000111'
#s2 = '001001101111001' out = 4

s1 = '010101010000111'
s2 = '001001101111001'
count = 0
i = 0
while i < len(s1):
    if s1[i] == s2[i]:
        count += 1
    i += 1
print(count)