#       List Comprehension

ls = [1,2,3,4,5,6]

# print([i**2 for i in range(1,100)])


# newls = [] 

# newls = [i**2 for i in ls]
# print(newls)



l = ['rahul', 'shubham', 'starch', 'madma', 'malayalam']

# print([i.capitalize() for i in l])

# print([i.capitalize() for i in l if len(i) % 2 == 0])

# print([[i**2, i**3] for i in ls if i > 4])

print([i if i == i[::-1] else i.upper() for i in l])
