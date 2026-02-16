#Wap to check that the length of the  names stored inside the list is even or odd if even reverse it and append else append its length only


l = ['hello', 'ayush', 'shivam', 'nikhil', 'durgesh', 'tamanna']

print([i[::-1] if len(i) % 2 == 0 else len(i) for i in l])