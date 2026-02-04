#wap to get all the accurences of each elemtn in a given list

ls = ['red', 'green', 'green', 'red', 'yellow', 'orange', 'orange']

dictt = {}
i = 0

while i <len(ls):
    if ls[i] not in dictt:
        dictt[ls[i]] = 1
    else:
        dictt[ls[i]] +=1
    i+=1
print(dictt)