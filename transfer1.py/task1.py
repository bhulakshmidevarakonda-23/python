numbers=[25,30,20,40,15,25]
sum=0
for i in numbers:
    sum+=i
    if sum>=100:
        break
print(sum)