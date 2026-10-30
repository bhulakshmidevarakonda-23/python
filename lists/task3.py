n=[1,2,3,4,4,5,6,6,3]
unique=[]
for i in n:
    if i  not in unique:
        unique.append(i)
print(unique)