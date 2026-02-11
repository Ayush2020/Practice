#WAP to create a dictionary with element and its count pair

l = ['yellow', 'red', 'green', 'yellow', 'yellow', 'yellow', 'red', 'red', 'green', 'yellow', 'red','red', 'green']
dictt = {}

for i in l:
    if i not in dictt:
        dictt[i] = 1
    else:
        dictt[i] += 1
print(dictt)
