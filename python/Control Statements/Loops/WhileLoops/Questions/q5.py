#wap to count the numbers of occurences of a particular chararters in the given string

strr = input("Enter a number: ")
char = input("Enter a character: ")
count = 0
i = 0
while i < len(strr):
  if strr[i] == char:
    count += 1
  i += 1
print(count)
  