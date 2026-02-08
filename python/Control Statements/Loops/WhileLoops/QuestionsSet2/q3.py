#Check it is a nagram


s1 = "silent"
s2 = "listen"

if len(s1) != len(s2):
  print("Not a Anagram")
else:
  i = 0
  while i < len(s1):
    j = 0
    found = False
    while j < len(s2):
      if s1[i] == s2[j]:
        found = True
        break
      j += 1
    if not found:
      print("Not a Anagram")
      break
    i+=1
  if found == True: 
    print("Anagram")
