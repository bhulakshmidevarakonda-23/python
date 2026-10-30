#reduce is advanced function and it is builtinfunction in python functools
#syntax:reduce(fun,iterable)
#it perform rolling on sequential of iterations
list1=[1,2,3,4,5,6,7,8,9,8,7,6,5,4]
from functools import reduce
result=reduce(lambda a,b:a+b,list1)
print(result)#75