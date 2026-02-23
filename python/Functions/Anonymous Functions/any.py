
# //? Lambda Functions

# add = lambda x, y : x + y
# print(add(10,20))


# sqr = lambda x : [x**2, x **3]
# print(sqr(3))



# convertLower = lambda x, y : (x + y).lower()
# final = convertLower("heLLO", "BuddY")
# print(final)


# //! v-n = lambda args : TSB if cond else FSB

# func = lambda x : x**2 if x % 2 == 0 else x**3
# print(func(9))

# func = lambda x : 'even length ' if len(x) % 2 == 0 else 'pallindrome' if x == x[::-1] else 'not'
# print(func("madam"))



# (lambda x : print(x**2))(3)
sqr = lambda *x : {i**2 : i**3 for i in x if i  % 2 == 0}
print(sqr(1,2,3,4,5))
