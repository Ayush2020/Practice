#WAP  to check that the input is tupple then check it have any middle value or not then middle element is of String datatype
#type and starrting with vowel and it should have length > 8


data = eval(input("Enter Data: "))

if type(data) == tuple:
    if len(data) % 2 != 0:
        mid = data[len(data)//2]
        if type(mid) == str:
            if mid[0] in 'aeiou':
                if len(mid) > 8:
                    print("Tuple, midle value, String, Vowel, Len > 8")
                else:
                    print("Smaller then 8 llenggth")
            else:
                print("Not Starts wiht any vowel")
        else:
            print("Not a String type")
    else:
        print("Not have any mid Value")

else:
    print("not an Tuple")