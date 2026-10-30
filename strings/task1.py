s = "Python is amazing"
n = ""

for i, ch in enumerate(s):
    if i % 2 != 0:
        continue
    else:
        n += ch

print(n)
