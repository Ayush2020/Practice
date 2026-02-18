#Check that the given character is a special character or a alphabet or a digit 


ch = input("Enter the ch--> ")

def character_check(ch):
  if  'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
    return "Alphabet"
  elif '0' <= ch <= '9':
    return "Digit"
  else:
    return "Special Char"
  
print(character_check(ch))