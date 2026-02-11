#WAp to create a dictionary and traverse into it and if the length is even point as it else it reverse it


names = {'apple', 'google','yahoo', 'microsoft','gmail','walmart'}

dictt = {}


for i in names:
  if len(i) % 2 == 0:
    dictt[i] = i
  else:
    dictt[i] = i[::-1]
    
print(dictt)