#Check that the given two strings are anagram strings or not


s1 = "silent"
s2 = "listen"

i = 0

while i < len(s1):
    j = 0
    found = False
    while j < len(s2):
        if s1[i] == s2[j]:
            found = True
            break
        j += 1
    
    if not found:
        print("Not Anagram ")
        break
    i += 1
else:
    print("Anagram")