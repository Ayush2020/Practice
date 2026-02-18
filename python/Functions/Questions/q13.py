#WAP to get the output :--> 
#s = 'hello buddy how are you'
#out = {h : [hello, how], b : [buddy], a:[are], y:[you]}

s = 'hello buddy how are you'

dictt = {}
s = s.split()

def strr(s):
  for i in s:
    if i[0] not in dictt:
      dictt[i[0]] = []
    dictt[i[0]].append(i)
  return dictt

print(strr(s))