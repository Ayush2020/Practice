# WAP to search for a particular character in a given string both of them should be taken from user as a argument RETURN THE INDEXES OF EACH OCCURENCES

strr = input("Enter the String:-->")
ch = input("Enter the character: --> ")


def ch_occur(strr,ch):
  ls = []
  for i in range(0,len(strr)):
    if ch == strr[i]:
      ls.append(i)
    else:
      return "Not Founnd"
  return ls
    
    
print(ch_occur(strr, ch))
