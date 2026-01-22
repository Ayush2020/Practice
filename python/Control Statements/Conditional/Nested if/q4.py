#WAP to find middle element is even nor odd take list from user first check tha there is any middle element is there or not
#s = [3,4,6,2,9,1,5]


lst = eval(input("Enter the List: "))

if len(lst) % 2 != 0:
  mid = lst[len(lst)//2 ]
  if type(mid) == int:
    if mid % 2 == 0:
      print("Middle Element is Even")
    else:
      print("Element is odd")
else:
  print("Even list")