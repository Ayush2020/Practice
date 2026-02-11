#WAP to find the sum of same indexed value from two different list

l1 = [1,2,3,4,5,6]
l2 = [1,2,3,4,5,6]
sumls = []

for i in range(len(l1)):
    for j in range(len(l2)):
        if l2[j] == l1[i]:
            sumls.append(l2[j] + l1[i])

print(sumls)