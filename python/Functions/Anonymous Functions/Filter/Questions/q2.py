
# //! WAP to fetch only the even length strings from a list of names given by user


print(list(map( lambda x : x,filter(lambda x : len(x) % 2 == 0, eval(input("Enter the String List : --> "))))))