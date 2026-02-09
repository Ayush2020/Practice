#WAp to check how many words are present in the given list

s = "hello world sentence"

count = 0
for i in s.split():
    count += 1
    print(i)

print("Counted Words: ",count)