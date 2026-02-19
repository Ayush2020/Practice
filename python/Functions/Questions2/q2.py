#WAF to search for a given character in the given string from user and return its index


user = input("enter the str: --> ")
ch = input("Enter the ch: --> ")

def search_ch(user, ch):
  for i in range(len(user)):
    if ch == user[i]:
      return i, "Index of the character"
  else:
    return"No such string"

print(search_ch(user, ch))