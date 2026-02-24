
#//! WAP to make a pair of names and ages

names = ['x','y','z']
age = ['a','b','c']
# out = [(x,a)]


var = lambda x,y : (x,y)

res = map(var, names,age)
print(list(res))


