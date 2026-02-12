#1 . [[1,2,3,"hello"][100,200,300][10,20,30]] interval = 6, interval = 600, interval = 60 external = 666


l = [[1,2,3,"hello"],[100,200,300],[10,20,30]]


external = 0
for i in l:
  if type(i) == list:
    internal = 0
    for j in i:
      if type(j) == int:
        internal +=j
    print("internal:", internal)
    external += internal
print("external: ", external )
