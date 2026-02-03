#WAP  to extract all the vowels and digits from a given string without using inbuilt functions
#s = 'he5llo@123' out = eo5123 first vowels and then digit

strr = 'he5llo@123'

i = 0
vowels = ""
digit = ""


while i < len(strr):
    if strr[i] in 'aeiou':
        vowels += strr[i]
    elif strr[i] in '0123456789':
        digit += strr[i]
    i+=1
print(vowels + digit)



