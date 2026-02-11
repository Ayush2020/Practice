#in zip data is lost so for saving the data we use zip_longest  
# zip_longest : same like zip :--> prevents data lost

from itertools import zip_longest

ls1 = [10, 20, 30]
ls2 = [1,2,3,4]
str = "helllo"
# print(list(zip_longest(ls1, ls2, str, fillvalue=0)))



#Print the same index values sum
for i, j, k in zip_longest(ls1, ls2, str, fillvalue=0):
  print(f" Sum of  {i} + {j} + {k} ---> {i + j + ord(k)}")
