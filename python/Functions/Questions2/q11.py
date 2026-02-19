#wap to extract of vowels from each word of a string 
s = 'hello buddy how are you'


def check(s):
  s = s.split()
  dictt = {} 

  for i in s:
    rev = ""
    for j in i:
      if j in 'aeiou':
        rev += j
    dictt[i] = rev
  return dictt

print(check(s))