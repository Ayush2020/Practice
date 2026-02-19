#WAF to return the length of a given argument if its collection datatype

data = eval(input("Enter the data:---> "))

def check(data):
  if  type(data) in [str, dict, list, set, tuple]:
    return "Length o Data--> ",len(data)
  else:
    return "Not a collection DT"

print(check(data))