
#//! s = 'good morning'
# {'good':GD, 'morning': "MG"}


out = lambda x: {x: (x[0]+ x[-1]).upper()}

res = map(out, "good morning".split())
print(list(res))