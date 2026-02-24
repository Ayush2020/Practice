
#//! WAp to get the folwwoing output
s = 'good morning'

out = lambda x : {x: x.upper()}
res = map(out, s.split())
print(list(res))