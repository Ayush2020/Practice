# local, global, non-local scopes

# //? local vars :--> the variable access only inside a block in which they are defined.!

# def func():
#   a = 200
#   print("Inside Func: --> ", a)
# func()
# print("outside func: --> ", a)


# //* Global Vars:---> the variable which access anywhere in the whole file.

# a = 100
# def func():
#   global a
#   a = 200
#   print("Inside Func: --> ", a)
# func()
# print("outside func: --> ", a)




#//! Non-Local vars:---> the variable which access inside the nested blocks

# def func():
#   a = 100
#   def inner():
#     # nonlocal a
#     a = 200
#     print("Inside inner : --> " , a)
    
#   inner()
#   print("Inside Outer --> ", a)

# func()



# a = 100
# def func():
#   global a
#   a = 120
#   def inner():
#     global a
#     a = 222
#     print("Inside inner --> ", a)
#   inner()
#   print("Inside outer : --> ",a)
  
# func()
# print("Outside--> ", a)