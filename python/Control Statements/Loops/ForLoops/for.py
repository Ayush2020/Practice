#[10 ,20, 30] -->
ls = eval(input("Enter:-"))

# newLs = []
#
# for i in range(len(ls)):
#     newLs += [(i, ls[i])]
#
# print(newLs)


print(list(enumerate(ls)))



# ls1 = [10, 20, 30]
# ls2 = (1,2,3)
# str = "hel"

#output --> [(20, 2, 'h), (30, 3, 'e'), (10, 1, 'l'), (20, 2, 'l'), (30, 3, 'o')]

# output = []
# for i in range(len(ls1)):
#     output.append((ls1[i], ls2[i], str[i]))
# print(output)

#ZIp -->  Used to bind values from collection of same indexes it return address so typecast it or runs a loop
#If length is mismatched it leads to data lost


# print(list(zip(ls1, ls2, str)))
# for i, j, k in zip(ls1, ls2, str):
#     print(f"I: {i} v:{j} v:{k}")