#WAP to find the square of all the elements present inside 
# the list

ls = [2,4,5,6,7,8,9]
ls2 = []
def square(ls):
  for i in ls:
    a = i**2
    ls2.append(a)
  return ls2

print(square(ls)) 
