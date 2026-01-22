#WAP to check that th einput is tuple then check it have any middle value or not then middle element is of string datatype
#it should be in a pallindrome and si should have length  > 8


data = eval(input("Enter Data: "))

if type(data) == tuple:
    if len(data) % 2 != 0:
        mid = data[len(data)//2]
        if type(mid) == str:
            if mid == mid[::-1]:
                if len(mid) >= 8:
                    print("String is tuple , Had mid value , String Datatype , Palindrome , length >= 8")
                else:
                    print("Middle Length is smaller than 8")
            else:
                print("Middle Not a palindrome")
        else:
            print("Middle is not a String")
    else:
        print("Not a Odd")
else:
    print("Data is not a tuple")