#Skipp al vowels from collections 

strr = 'applebanana'

i = 0
while i < len(strr):
  if strr[i] in "aeiouAEIOU":
    i+=1
    continue
  print(strr[i])
  i+=1