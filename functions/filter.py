#syntax:filter(function,iterable)
#def even(a):
 #   return a%2==0
#obj=even(24)
#print(obj)#true
#in filter only:
#list1=[1,2,3,4,5,6,7,8,9,14,35,46,57]
#def even(a):
   # return a%2==0
#result=filter(even,list1)
#print(list(result))#[2, 4, 6, 8, 14, 46]
# in filter with lambda:
#list1=[1,2,3,4,5,6,7,8,9,14,35,46,57]
#result=filter(lambda a:a%2==0,list1)
#print(list(result))#[2,4,6,8,14,46]