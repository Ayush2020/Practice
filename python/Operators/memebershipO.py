#  membership Operators which are in or not in 

a = 10
type(a) == int or type(a) == float or type(a) == bool

type(a) in [int, float, complex, bool]

isinstance(a, str)

isinstance(a, int)

b = (int, float, str, bool, complex)



# isinstance only store datatypes in the form of tuple
 
c = isinstance(a, b)
print(c)