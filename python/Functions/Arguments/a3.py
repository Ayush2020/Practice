# def func(**kwargs):
#   newls = []
#   for i, j in kwargs.items():
#     if i == 'male':
#       newls.append(f"Mr {j}")
#     elif i == 'female':
#       newls.append(f"Mrs {j}")
#   return newls

# print(func(male = 'rahul', female = "sanjana"))



def func(**kwargs):
  return [f'Mr {i}' if j.lower().strip() == 'male' else f"Miss {i}" for i, j in kwargs.items()]

print(func(rahul = 'male', abbir='female', nikhil = 'female', durgesh = 'female'))




