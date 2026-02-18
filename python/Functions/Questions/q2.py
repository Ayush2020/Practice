# WAP to check that the string is pallindrome or not 
#take user input without slicing 

# def is_palindrome(s):
#     s = s.lower()
#     n = len(s)
    
#     for i in range(n // 2):
#       if s[i] != s[n - 1 - i]:
#         return False
#       return True
  
  
# user = input("Enter the String: --> ")

# if is_palindrome(user):
#   print(f"{user} is pallindrome")
# else:
#   print(f"{user} is not pallindrome")



def pal_check(strr):
  newstr = ""
  for i in strr:
    newstr = i + newstr
  if strr == newstr:
    print("Pallindrome")
  else:
    print("not a pallindrome")
    
    
c = pal_check("malayalam")