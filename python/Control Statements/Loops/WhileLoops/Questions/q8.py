# get all the occurences of a character in a given string if its present otherswise not found


strr = input("Enter a string: ")
dict = {}

i = 0
while i < len(strr):
    if strr[i] not in dict:
        dict[strr[i]] = 1
    else:
        dict[strr[i]] += 1
    i+=1
print(dict)

