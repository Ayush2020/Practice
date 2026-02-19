#Wap to return a list of square of all the elements from a list


ls = eval(input("ENter the list--> "))
def square(ls):
  newls = []
  for i in ls:
    sqr = i ** 2
    newls.append(sqr)
    
  return newls

print(square(ls))
  