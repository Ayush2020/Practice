
# //! WAP to fetch the names from a list whose first letter is a consonant

print(list(map( lambda x : x,filter(lambda x : x[0].lower() not in 'aeiou', eval(input("Enter the List of Strings-->"))))))