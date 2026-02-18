#WAF to get the output 
s = ["random.txt", "hello.py", "functions.py",
     "hii.html", "howw.html"]

# out = {txt: [random], py : [fucntions, hello]}
dictt = {}


def strr(s):
  for i in s:
    name, ext = i.split('.')
    if ext not in dictt:
      dictt[ext] = []
    dictt[ext].append(name)
  
  return dictt

print(strr(s))