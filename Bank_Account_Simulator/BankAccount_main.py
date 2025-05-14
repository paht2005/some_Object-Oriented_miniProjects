class Account:
    def __init__(self, owner_name, start_balance=0.0):
        self.owner_name = owner_name
        self.balance = start_balance

    def add_funds(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Added ${amount:.2f}. Current balance: ${self.balance:.2f}")
        else:
            print("Amount must be positive!")

    def take_funds(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
            else:
                print("Not enough funds.")
        else:
            print("Withdrawal must be greater than zero!")

    def print_info(self):
        print("\n[Account Summary]")
        print(f"Owner: {self.owner_name}")
        print(f"Balance: ${self.balance:.2f}")


# Data Store
account_list = {}

def register_account():
    holder = input("Enter your full name: ").strip()
    try:
        initial = float(input("Initial deposit amount: "))
    except ValueError:
        print("Invalid input. Start balance set to $0.")
        initial = 0.0
    new_acc = Account(holder, initial)
    account_list[holder] = new_acc
    print(">> Account successfully created.")

def login_account():
    holder = input("Enter account name: ").strip()
    acc = account_list.get(holder)
    if acc:
        while True:
            print("\n[Account Panel]")
            print("1. Add Money")
            print("2. Withdraw Money")
            print("3. View Account Info")
            print("4. Logout")
            action = input("Choose action (1-4): ")

            if action == '1':
                try:
                    amt = float(input("Enter amount to deposit: "))
                    acc.add_funds(amt)
                except ValueError:
                    print("Invalid number.")
            elif action == '2':
                try:
                    amt = float(input("Enter amount to withdraw: "))
                    acc.take_funds(amt)
                except ValueError:
                    print("Invalid number.")
            elif action == '3':
                acc.print_info()
            elif action == '4':
                print("Logging out...")
                break
            else:
                print("Invalid option.")
    else:
        print("Account not found.")

# App Menu
def run_simulator():
    while True:
        print("\n=== Welcome to SimpleBank ===")
        print("1. Open New Account")
        print("2. Access Existing Account")
        print("3. Exit")
        option = input("Select (1-3): ")

        if option == '1':
            register_account()
        elif option == '2':
            login_account()
        elif option == '3':
            print("Thanks for using SimpleBank. Goodbye!")
            break
        else:
            print("Please select a valid option.")

# Start App
run_simulator()
