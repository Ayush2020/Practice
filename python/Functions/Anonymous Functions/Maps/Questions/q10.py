
#//! Find the cuberoot of all the elements form of a range given by users in a single line



var = lambda x : x**1/3

res = map(var, (i for i in range(int(input("Enter the range: --> ")))))
print(list(res))