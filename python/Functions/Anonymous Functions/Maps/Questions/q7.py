
#//* WAP to get the following output s = 'good morning' --> {'good':4, 'morning':7}


var = lambda x : {x :len(x)}

res = map(var,'good morning'.split())
print(list(res))