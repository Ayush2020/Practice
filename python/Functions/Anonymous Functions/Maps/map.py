
# a = lambda x : x**2
# print(a(2))



# a = lambda x : x**2
# ls = [1,2,3,4,5,6,7]

# print(list(map(a,ls)))



# a = lambda x: x**2
# res = map(a, [1,2,3,4,5,6,7])

# for i in res:
#   print(i, end=" ")


# def pallindrome(strr):
#   return strr == strr[::-1]

# print(list(map(pallindrome, ['random', 'madam', 'malayalam'])))




ls = [1,2,3,4,5,6]
ls2= [2,3,4,5,6]

var = lambda a, b: a + b
# print(var(10,20))

print(list(map(var, ls, ls2)))