# wap to check whether the given character is uppercase/ lowercase/ digit / speicail (without using inbuilt fucntion)
# )
# Extra :- for a character IF uppercase return lowercase if lowercase return uppercase -> ord chr

char = input("Enter a character: ")

if char >= 'A' and char <= 'Z':
    print("Uppercase")
    print("Lowercase:", chr(ord(char) + 32))
elif char >= 'a' and char <= 'z':
    print("Lowercase")
    print("Uppercase:", chr(ord(char) - 32))
elif char >= '0' and char <= '9':
    print("Digit")
else:
    print("Special Character")
