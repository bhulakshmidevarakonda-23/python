age=int(input("enter age:"))
try:
    if age<18:
        raise Exception("not eligible")
    print("Eligible")
except Exception as e:
    print(e)