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




#Approach 2
# dictt1 = {}
# dictt2 = {}



# if len(s1) != len(s2):
#     print("Not anagram")
# else:
#     i = 0
#     j = 0
#     while i < len(s1):
#         if s1[i] not in dictt1:
#             dictt1[s1[i]] = 1
#         else:
#             dictt1[s1[i]] += 1
#         i+=1
    
    
#     while j < len(s2):
#         if s2[j] not in dictt2:
#             dictt2[s2[j]] = 1
#         else:
#             dictt2[s2[j]] += 1 
#         j+=1
    
#     if dictt1 == dictt2:
#         print("Anagram")
#     else:
#         print("not an Anagram")