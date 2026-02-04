# #Break the string at 2nd vowels comes

strr = "AppleBanana"

i = 0
count = 0
while i < len(strr):
  if strr[i] in 'aeiouAEIOU':
    count +=1
    if count == 2:
      break
  i+=1
print(strr[:i])
    
