
class Bank:
    def __init__(self):
        self.accounts = {}
        self.username = ""
        self.password = ""
        self.balance = 0
        self.statement = []

    def create_account(self):
        username = input("Create username: ")

        if username in self.accounts:
            print("Account already exists!")
            return

        password = input("Create password: ")

        self.accounts[username] = {
            "password": password,
            "balance": 0,
            "statement": []
        }

        print("Account created successfully!")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if (username in self.accounts and
                self.accounts[username]["password"] == password):

            self.username = username
            self.password = password
            self.balance = self.accounts[username]["balance"]
            self.statement = self.accounts[username]["statement"]

            print("Login successful!")
            self.menu()

        else:
            print("Invalid username or password!")

    def deposit(self):
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            self.balance += amount
            self.statement.append("Deposited: " + str(amount))
            self.accounts[self.username]["balance"] = self.balance
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount <= self.balance:
            self.balance -= amount
            self.statement.append("Withdrawn: " + str(amount))
            self.accounts[self.username]["balance"] = self.balance
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print("Available balance:", self.balance)

    def mini_statement(self):
        print("\n--- Mini Statement ---")

        if len(self.statement) == 0:
            print("No transactions yet!")
        else:
            for item in self.statement:
                print(item)

        print("Available balance:", self.balance)

    def menu(self):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Mini Statement")
            print("5. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                self.mini_statement()
            elif choice == "5":
                print("Logout successful!")
                break
            else:
                print("Invalid choice!")


class User(Bank):
    def account(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("Thank you!")
                break
            else:
                print("Invalid choice!")


obj = User()
obj.account()
