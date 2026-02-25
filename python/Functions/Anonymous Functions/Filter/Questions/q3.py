
#//! WAp to fetch only tht flowers from this string given collections

ls = ['sun flower', 'hello', 'banana tree', 'lily flower', 'marigold flower', 'mango tree', 'lotus flower']

print(list(filter(lambda x : 'flower' in x, ls)))