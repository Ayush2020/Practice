
# //? Filter --> 

# ls = [1,2,3,5,6,7,8]

# print(list(filter(lambda x : x % 2 == 0 and x > 2, ls)))



# def func(strr):
#   if strr == strr[::-1]:
#     return 1
#   else:
#     return 0
  
  
# print(list(filter(func, ["rahuk", 'madam', 'malayalam', 'sherr'])))




# print(list(filter(lambda x : x, [None, [], {}, 'hello', 12])))



# square = lambda x : x**2
# res = map(square, [1,2,3,4,5,6])
# data = filter(lambda x: x% 2 == 0, res)
# print(list(data))




# print(list(filter(lambda x : x%2 == 0,map(lambda x : x**2, range(1,11)))))