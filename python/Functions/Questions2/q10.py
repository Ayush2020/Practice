#Get this output
s = 'hai hello how are you'
# out = 'iah olleh woh era uoy'

def rv(s):
  s = s.split()
  rev = ""
  for i in s:
    for j in range(len(i) - 1, -1, -1):
      rev += i[j]
    rev += " "
  return rev

print(rv(s))
