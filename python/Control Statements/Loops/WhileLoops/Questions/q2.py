#wsp to print both upper case and lower case charcaters A a B b C c

i = ord('A')
while(i <= ord('Z')):
    print(chr(i), end=" ")
    print(chr(i + 32), end=" ")
    i+=1