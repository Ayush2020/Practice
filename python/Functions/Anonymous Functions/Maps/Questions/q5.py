
#//! WAP to print the values from a list if its multivalued datatype

var = lambda x : x if type(x) in [list, tuple, set,dict, str] else None

res = map(var, ["Strinf",{1,2,3,4}, [1,2,34], 1, 1.43])
print(list(res))