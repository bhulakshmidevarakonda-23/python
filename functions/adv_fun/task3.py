n=int(input("enter a number:"))
from functools import reduce
fact=reduce(lambda x,y:x*y,range(1,n+1))
print(fact)