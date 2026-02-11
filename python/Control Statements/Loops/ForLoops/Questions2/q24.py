#WAP to pair the values of two dictionary

dict1 = {1:"h1", 2:"h2", 3:"h3"}
dict2 = {4:"h4", 5:"h5", 6:"h6"}

for i, j in zip(dict1.values(), dict2.values()):
  print(i, j)
  
  