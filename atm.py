balance=20000
def pin():
    num=int(input("enter a pin number:"))
    if num==1234:
        print("pin number is correct")
        return True
    else:
        print("incorrect pin number")
        return Flse



def deposit():
    global balance
    
    amount=int(input("enter amount:"))

    if amount>0:
        balance+=amount
        print("amount deposit successfully")
    else:
        print("enter positive")

def withdraw():
    global balance
    amount=int(input("enter amount:"))
    if balance>=amount:
       if amount>0:
          balance-=amount
          print("amount withdraw successfully")
       else:
           print("enter positive")
    else:
        print("insufficient balance")

def balance_enquiry():
    print(f"chech balance:{balance}")
def exit():
    print("exit")
if pin():
  while True:
    
    print("2.deposit")
    print("3.withdraw")
    print("4.balance_enquiry")
    print("5.exit")
    choice=int(input("enter choice:"))
    if choice==1:
        pin()
    elif choice==2:
        deposit()
    elif choice==3:
        withdraw()
    elif choice==4:
        balance_enquiry()
    elif choice==5:
        exit()
        break
    else:
        print("invalid")
    


