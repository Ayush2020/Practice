
#//! Fetch only palindrome strings from a given list --> no slicing
print(list(filter(lambda x : x == ''.join(reversed(x)), eval(input("Enter the list --> ")))))