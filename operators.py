num1=500
num2=500
#arthmatic
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1**num2)
print(num1//num2)
#comparision
print(num1==num2)
print(num1!=num2)
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)
#identity
print(num1 is num2)
print(num1 is not num2)
#logical
print(num1 > 0 and num2 > 0)
print(num1 > 0 or num2 > 0)
print(not num1 > 0)
#membership
print(num1 in [num2])
print(num1 not in [num2])
#discount calculation
p1=1000
discount=10
result=p1*(discount)/100

p1=p1-result
print("product cost:", p1)
#formatting
print(f"discount given {discount}% final discount {result} after discount {p1}")
print(base value)