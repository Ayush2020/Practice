#WAP to extract only individual data types from the list


l = [1, 1.224, (1 + 2j), "String", [1,2,3], (1,2,3), True]
newls = []

for i in range(len(l)):
    if type(l[i]) in [int, float, complex, bool]:
        newls.append(l[i])

print("Indivual Data: ", newls)
