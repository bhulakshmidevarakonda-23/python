n1 = [1, 2, 2, 3, 4, 4, 5]
n2=[]
for i in n1:
    if i not in n2:
        n2.append(i)
print(n2)