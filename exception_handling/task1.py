
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

try:
    c = a - b
    if c < 0:
        raise Exception("Negative number")
    print(c)

except Exception as e:
    print(e)
