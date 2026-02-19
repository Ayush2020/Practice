#WAP to extract all the int numbers present at odd index only if its divisible by 5 from a list 


data = eval(input("enter the list: --> "))

def extract_number(data):
  newls = []
  for i in range(0, len(data)):
    if i % 2 != 0:
      for j in data:
        if j % 5 == 0:
          newls.append(i)
  return newls

print(extract_number(data))