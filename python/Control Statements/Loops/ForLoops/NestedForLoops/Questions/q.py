# "hello buddy how" -- > "olleh yddub woh" without inbuilt function and slicing

s = "hello buddy how"

s = s.split()

out = ""

for i in s:
    for j in range(len(i) - 1, -1, -1):
        out += i[j]
    out += " "

print(out.strip())
