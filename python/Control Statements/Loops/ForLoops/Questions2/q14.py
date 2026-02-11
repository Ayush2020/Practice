#WAP to find the  sum of all the umbers present inside a given string

s = 'hel123ollo543'

summ = 0

for i in s:
    if i in '0123456789':
        summ += int(i)

print(summ)