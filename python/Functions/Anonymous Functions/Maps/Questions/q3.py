
# //! WAP to print the sum of same indexed values from two lists

idx = lambda x, y: x+y

res = map(idx, [2,3,4,5,6], [1,2,3,4,5])
print(list(res))