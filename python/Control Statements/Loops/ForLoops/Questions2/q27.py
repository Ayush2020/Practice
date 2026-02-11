l = [10 , 20, 30, [1,2,3]]
# 10,20,30,1,2,3

for i in l:
  if type(i) == list:
    for j in i:
      print(j)
  else:
    print(i)
