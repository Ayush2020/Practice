# [1,0,0,2,0,4,0,3,9,0, 0,5] right shift zeros to thee end
# [1,2,4,3,9,5,0,0,0,0,0,0] #Without append and inbuilt functions

ls = [1, 0, 0, 2, 0, 4, 0, 3, 9, 0, 0, 5]

#With Inbuilt functions
# l = []

# for i in ls:
#   if i != 0:
#     l.append(i)
# for i in range(len(ls)):
#   if i < len(l):
#     ls[i] = l[i]
#   else:
#     ls[i] = 0

# print(ls)


# Without inbuilt functions
j = 0
for i in range(len(ls)):
    if ls[i] != 0:
        ls[i],ls[j] = ls[j], ls[i]
        j += 1

print(ls)
        