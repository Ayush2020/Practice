#VAriable length positional argument : (*args) -->
# packs all the value under a single argument 
#It will returns in the form of tuple --> if i have to get values we can use indexing or we can use loop in it
#if we wont pass argument it wont give error it just returns an empty tuple 



def func(*args):
  return args, type(func)

print(func(1001, 10, 20, "hello"))