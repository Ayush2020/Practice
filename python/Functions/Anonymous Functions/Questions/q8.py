
#//! wap to check that the string is pallindrome or not if not then check even length or not if even return uppercase otherwise return swapcase of that string if pallindrome directly return pallindrome 

str_check = lambda x : f'{x} is pallindrome' if x == x[::-1] else x.upper() if len(x) % 2 == 0 else x.swapcase() 

print(str_check("hellLLo"))
print(str_check("Python"))
print(str_check("madam"))
