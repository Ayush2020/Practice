#WAP to extract only collection data types from the list


l = [1, 1.224, (1 + 2j), "String", [1,2,3], (1,2,3), True]

newls = []

for i in range(len(l)):
    if type(l[i]) in [str, list, tuple, set, dict]:
        newls.append(l[i])

print(newls)
