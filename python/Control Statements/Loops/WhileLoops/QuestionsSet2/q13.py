#Filter all the flowers from the given list

L = ['banya tree', 'rosemary flower', 'lotus flower', 'mango tree', 'lavender flower']

i = 0
newls = []

while i< len(L):
    if 'flower' in L[i]:
        newls.append(L[i])
    i+=1

print(newls)