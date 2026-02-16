#WAP to check that the  type of element is individual or collection if
# collection reverse it else returns  the square of that

l = [1, 1.044, (2+3j), "String", [1,2,3], (1,2,3)]

newls = [[i**2 if type(i) not in (str, list, set,dict,tuple) else i[::-1] for i in l]]
print(newls)

