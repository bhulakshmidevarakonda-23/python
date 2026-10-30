
class atm:
    def __init__(self, bank, location, branch, balance):
        self.bank = bank
        self.location = location
        self.branch = branch
        self.balance = balance

    def display(self):
        print("Bank:", self.bank)
        print("Location:", self.location)
        print("Branch:", self.branch)

    def credit(self):
        amount = int(input("Enter amount: "))
        if amount > 0:
            self.balance += amount
            print(f"{amount} credited successfully")
        else:
            print("Invalid amount")

    def debit(self):
        amount = int(input("Enter amount: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"{amount} debited successfully")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Balance is {self.balance}")

    def choice(self):
        while True:
            print("\n1. Bank")
            print("2. Credit")
            print("3. Debit")
            print("4. Check balance")
            print("5. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                self.display()
            elif choice == 2:
                self.credit()
            elif choice == 3:
                self.debit()
            elif choice == 4:
                self.check_balance()
            elif choice == 5:
                print("Exit successfully")
                break
            else:
                print("Invalid choice")


obj = atm("SBI", "Chennai", "T Nagar", 5000)
obj.choice()
