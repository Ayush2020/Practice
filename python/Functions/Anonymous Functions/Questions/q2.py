
# //! WAP to check that the given string is pallindrome or not


is_pallin = lambda x : 'pallindrome ' if x == x[::-1] else 'not pallindrome'
print(is_pallin("madam"))
