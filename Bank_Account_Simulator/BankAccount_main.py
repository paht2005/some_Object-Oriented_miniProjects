class BankAccount:
    def __init__(self, name, opening_balance=0.0):
        self.name = name
        self.balance = opening_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f">> Deposited: ${amount:.2f}")
            print(f"   New Balance: ${self.balance:.2f}")
        else:
            print(">> Error: Deposit must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f">> Withdrawn: ${amount:.2f}")
                print(f"   Remaining Balance: ${self.balance:.2f}")
            else:
                print(">> Error: Insufficient balance.")
        else:
            print(">> Error: Amount must be greater than zero.")

    def display_info(self):
        print("\n=== Account Details ===")
        print(f"Holder Name: {self.name}")
        print(f"Balance: ${self.balance:.2f}")


# Global Account Storage
user_accounts = {}


def create_account():
    name = input("Enter full name to create account: ").strip()
    try:
        balance = float(input("Enter opening balance: "))
    except ValueError:
        print(">> Invalid input. Starting with $0.00.")
        balance = 0.0
    user_accounts[name] = BankAccount(name, balance)
    print(">> New account has been created.")


def access_account():
    name = input("Enter your account name: ").strip()
    account = user_accounts.get(name)
    if not account:
        print(">> No matching account found.")
        return

    while True:
        print("\n--- Account Menu ---")
        print("1. Deposit Funds")
        print("2. Withdraw Funds")
        print("3. Show Account Info")
        print("4. Return to Main Menu")
        choice = input("Select option (1-4): ")

        if choice == '1':
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print(">> Invalid input. Must be a number.")
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print(">> Invalid input. Must be a number.")
        elif choice == '3':
            account.display_info()
        elif choice == '4':
            print("Returning to main menu...")
            break
        else:
            print(">> Invalid selection.")


def launch_bank_app():
    while True:
        print("\n==== MiniBank System ====")
        print("1. Create New Account")
        print("2. Login to Account")
        print("3. Quit")
        main_choice = input("Choose (1-3): ")

        if main_choice == '1':
            create_account()
        elif main_choice == '2':
            access_account()
        elif main_choice == '3':
            print(">> Thank you for banking with us!")
            break
        else:
            print(">> Invalid input. Please try again.")


# Launch app
if __name__ == "__main__":
    launch_bank_app()
