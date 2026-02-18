#WAP the numbers of same bits of same length strings

s1 = '010101010000111'
s2 = '001001101111001'



def counter(s1, s2):
  count = 0
  for i in range(0,len(s1)):
    if s1[i] == s2[i]:
      count += 1
  return count

print(counter(s1,s2))