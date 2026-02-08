#wap to print namesonly of he length of them is even

L = ['vaidegi', 'rahul', 'jai', 'veer', 'apple', 'vansh', 'elephant', 'umbrella']

i = 0
while i < len(L):
    if len(L[i]) % 2 == 0:
        print(L[i])
    i+=1