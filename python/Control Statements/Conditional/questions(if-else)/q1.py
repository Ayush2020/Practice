#IF _ELSE

# WAP to check that the given character is upper case if yes return lower case else return uppecase

char = input("Enter the Char: ")

if "a" <= char <= "z":
    print(chr(ord(char) - 32))
else:
    print(chr(ord(char) + 32))