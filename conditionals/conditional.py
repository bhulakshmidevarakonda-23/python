#if
#use when condition is true
#syntax
#if condition:
 #statements

#if 5>2:
      #print("Five is greater than two!")
#else
#use when condition is false
#n1="bhulu"

#n2="cocktail"
#if n1=="bhulu" and n2=="cocktail":
    #print("success")
#else:
    #print("failure")
#elif else if
#used to check multiple conditions
#syntax
#if condition1:
    #statements
#elif condition2:
    #statements
#elif condition3:
    #statements
#else:
#n = int(input("Enter your number: "))

#if n >= 7 and n <= 10:
    #print("Number is between 7 and 10")


#real life example
#user login : user registerd and after some time 
#user wants to login but enter credentials are wrong
 #but we donts know which is wrong like name or 
 #passwor or somthing.to overcome this type of 
 #problems this statements ARE USED
#username=input("Enter your username:")
#password=input("Enter your password:")
#if username == "bhulu":
    #if password == "2346":
       # print("login success")
    #else:
      #  #print("password is wrong")  
#else:
    #print("username is wrong")


#char=input("Enter your character:")
#vowels=['a','e','i','o','u','A','E','I','O','U']
#if char in "aeiouAEIOU":
   # print(f"{char} is a vowel")
#else:
  #  print(f"{char} is consonant")
#TASK-1
n=int(input("Enter your number:"))
if n % 2 == 0:
    print(f"{n} is even number")
else:
    print(f"{n} is not an even number")
#TASK-2
age=int(input("Enter your age:"))
if age>=0 and age<=12:
    print("You are a child")
elif age>=13 and age<=19:
    print("You are a teenager")
elif age>=20 and age<=59:
    print("You are an adult")
elif age>=60:
    print("You are a senior citizen")
else:
    print("Invalid input")
#TASK-3
n = int(input("Enter your number: "))
if n<0:
    print(f"Number is negative that is {n}")
elif n==0:
   print(f"Number is zero {n}")
elif n>0:
    print(f"Number is positive that is {n}")
else:
    print("Invalid input")

#TASK-4
year=int(input("Enter your year:"))
if year%4==0 and year%100!=0 or year %400==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
#TASK-5
n1=10
n2=10
op=input("Enter your operator(+,-,*,/,%,**,//):")
if op=="+":
    print("result:",n1+n2)
elif op=="-":
    print("result:",n1-n2)
elif op=="*":
    print("result:",n1*n2)
elif op=="/":
    print("result:",n1/n2)
elif op=="%":
    print("result:",n1%n2)
elif op=="**":
    print("result:",n1**n2)
elif op=="//":
    print("result:",n1//n2)
else:
    print("Invalid operator")






    