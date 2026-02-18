# fetch all the  prime numbers by the given list by user

ls = eval(input("Enter the List:-->"))
ls2 = []

def prime_num(ls):
  for i in ls:
    if i > 1:
      for j in range(2, i):
        if i % j == 0:
          print(f"{i},Not prime")
          break
      else:
        ls2.append(i)
  return "Prime Numbers in the given list--> ",ls2


print(prime_num(ls))