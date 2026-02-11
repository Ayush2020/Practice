#WAP to replace all the characters from a given string with "-"  which occurs more than once
#ex : --> helloai -> -e--o-ai



s = "hellohai"
result = ""

for i in s:
  if s.count(i) > 1:
    result += "-"
  else:
    result += i
print(result)
  