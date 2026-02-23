
# //! WAP to check that the given number is pallindrome or not 

num_check = lambda x : 'pallindrome' if str(x) == str(x)[::-1] else 'not '
print(num_check(1234321))