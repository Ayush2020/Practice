#WAP to check that the given number is a collection or not if collection return its reverse else return its square

user = eval(input("Enter the Data-->"))


def check_dt(user):
  if type(user) not in [str, dict, list, tuple, set]:
    return user**2
  else:
    return user[::-1]
    
print(check_dt(user))