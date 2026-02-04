#Check given string is panagram

s =  "the quick brown fox jumps over the lazy dog"
s = s.lower()

letter = set()
i = 0
while i < len(s):
    ch = s[i]
    if 'a' <= ch <= 'z':
        letter.add(ch)
    i+=1

if len(letter) == 26:
    print("panagram")
else:
    print("not a panagram")
