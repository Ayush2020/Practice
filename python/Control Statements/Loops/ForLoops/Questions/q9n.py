#Get the non default values from a given list

L = ["", 0, 0.0, None, [], {}, set(), "Hello", 1, 2.5, [1,2], (1,2), {1:2}, {1,2}]

newls = []
i = 0
for i  in L:
  if bool(i) == True:
    newls.append(i)

print(newls)