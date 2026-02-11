#WAP to remove all the duplicates from a list taken by user



l = ['yellow', 'red', 'green', 'yellow', 'yellow', 'yellow', 'red', 'red', 'green', 'yellow', 'red','red', 'green']
newls = []
for i in range(len(l)):
    if l[i] not in newls:
        newls.append(l[i])

print(newls)
