#Check that the middle element of a given list is string of even length and have first character is vowel

lst = eval(input("Enter the list : "))
mid_index = len(lst) // 2
mid_index = lst[mid_index]

if len(mid_index) % 2 == 0 and mid_index[0].lower() in ["a", "e", "i", "o", "u"]:
    print("First char is Vowel")
else:
    print("Not a vowel")

