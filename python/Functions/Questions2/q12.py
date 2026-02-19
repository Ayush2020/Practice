#Get the output
#s = 'python is very easy'
#out = {'python': pn, is : is, very: 'vy', easy:ey}


s = 'python is very easy'

def check(s):
  s = s.split()
  dictt = {}
  for i in s:
    if i not in dictt:
      dictt[i] = i[0] + i[-1]
      
  return dictt

print(check(s))