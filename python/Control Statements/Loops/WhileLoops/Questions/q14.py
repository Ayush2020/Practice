#wap to print the names from a list whose name is starting with a vowel


L = ['vaiheli', 'rahul', 'shivam', 'jai', 'veer', 'apple', 'vansh', 'elephant', 'manya', 'umbrella']

i = 0
while i < len(L):
    if L[i][0].lower() in 'aeiou':
        print(L[i], end=" ")
    i+=1
