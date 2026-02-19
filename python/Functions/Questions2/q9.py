# WAF to get the following output
#s = 'happy morning be safe'
# count vowels in easy word


s = 'happy morning be safe'


def vowels(s):
  dictt = {}
  s = s.split()

  for i in s:
    count = 0
    for j in i:
      if j in 'aeiou':
        count += 1
    dictt[i] = count
    
  return dictt

print(vowels(s))