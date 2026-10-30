#class calculator():
    #def add(self,a=10,b=2):
       # print(a+b)
    #def add(self,a=2,b=3,c=5):
        #print(a+b+c)
#obj=calculator()
#obj.add(5,5,2)#12
#class gfather():
   # def __init__(self, a):
       # self.__a = a#this is private ,that means only access for this class only because of (_,__)
       # print(f"this is base class {a}")
#class father(gfather):
    #def details(self):
        #print(f"this is derived class {self._gfather__a}")
#obj = father("100cr")
#obj.details()
#example in bank point user want to protect username,password ,which is private so use _,__
#class details(): 
   # def login(self,user,password):
       # self.__user=user
        #self.__passwor=password