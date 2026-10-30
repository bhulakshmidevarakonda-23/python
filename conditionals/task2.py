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