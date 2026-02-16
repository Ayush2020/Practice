#WAp to create a list contains sum of same indexed value  of two list taken from user as a input 

l1 = [1,2,3,4,5,6]
l2 = [1,2,3,4,5,6]

# Using list comprehension to sum same-indexed values
l3 = [a + b for a, b in zip(l1, l2)]
print(l3)
