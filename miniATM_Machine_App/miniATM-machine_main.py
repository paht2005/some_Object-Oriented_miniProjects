# Nguyen Cong Phat 
# Github: https://github.com/paht2005

# === SimpleBank ATM Simulation ===
#
# System Features:
# - Secure login using a 4-digit PIN.
# - View account balance.
# - Deposit funds into the account.
# - Withdraw funds with balance validation.
# - Change PIN securely.
# - Log out safely.
#
# Class Overview:
#
# 1. UserWallet
#    - Attributes:
#        + id (account number)
#        + __pin (private PIN)
#        + __funds (private account balance)
#    - Methods:
#        + show_funds(): display current balance
#        + add_funds(): deposit money
#        + take_funds(): withdraw money
#        + update_pin(): change the PIN securely
#
# 2. SimpleBankATM
#    - Manages account creation and authentication
#    - Provides the main interface for user interaction
#    - Handles core banking operations via a text-based menu
#
# Key Programming Concepts:
# - Encapsulation: Protects sensitive data like PIN and balance using private attributes.
# - Class Design: Separation of concerns between data (UserWallet) and control logic (SimpleBankATM).
# - Error Handling: Validates input formats and provides clear feedback on invalid operations.
# - User Experience: Console interface is intuitive and structured with clear options.
import sys

# === Account Class ===
class UserWallet:
    def __init__(self, acc_id, secret_pin, initial_funds=0):
        self.id = acc_id
        self.__pin = secret_pin
        self.__funds = initial_funds

    def _verify_pin(self, input_pin):
        return input_pin == self.__pin

    def show_funds(self):
        print(f"💰 Available Balance: {self.__funds}")

    def add_funds(self, amount):
        if amount > 0:
            self.__funds += amount
            print(f"✅ Deposited {amount}. Updated Balance: {self.__funds}")
        else:
            print("❌ Invalid deposit amount.")

    def take_funds(self, amount):
        if amount <= 0:
            print("❌ Withdrawal must be greater than 0.")
        elif amount > self.__funds:
            print("❌ Not enough funds.")
        else:
            self.__funds -= amount
            print(f"✅ Withdrawn {amount}. Remaining Balance: {self.__funds}")

    def update_pin(self, current, new_pin):
        if self._verify_pin(current) and new_pin.isdigit() and len(new_pin) == 4:
            self.__pin = new_pin
            print("🔐 PIN successfully updated.")
        else:
            print("❌ Failed to update PIN. Ensure correctness and 4-digit format.")

# === ATM Controller ===
class SimpleBankATM:
    def __init__(self):
        self.user_db = {}

    def open_account(self):
        print("\n📘 Open New Account")
        user_id = input("Enter a unique account ID: ")
        new_pin = input("Set a 4-digit PIN: ")

        if user_id in self.user_db:
            print("❌ Account already exists.")
            return

        if len(new_pin) == 4 and new_pin.isdigit():
            self.user_db[user_id] = UserWallet(user_id, new_pin)
            print("✅ Account registered.")
        else:
            print("❌ PIN must be exactly 4 numeric digits.")

    def login_account(self):
        print("\n🔐 Account Login")
        user_id = input("Account ID: ")
        input_pin = input("PIN: ")

        account = self.user_db.get(user_id)
        if account and account._verify_pin(input_pin):
            print("✅ Access granted.")
            self.account_operations(account)
        else:
            print("❌ Invalid credentials.")

    def account_operations(self, account):
        while True:
            print("\n===== 💳 Account Menu =====")
            print("1. View Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Logout")

            option = input("Choose (1-5): ")

            if option == "1":
                account.show_funds()
            elif option == "2":
                try:
                    amount = float(input("Enter amount to deposit: "))
                    account.add_funds(amount)
                except ValueError:
                    print("❌ Invalid input.")
            elif option == "3":
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.take_funds(amount)
                except ValueError:
                    print("❌ Invalid input.")
            elif option == "4":
                old_pin = input("Current PIN: ")
                new_pin = input("New 4-digit PIN: ")
                account.update_pin(old_pin, new_pin)
            elif option == "5":
                print("🚪 Logging out...")
                break
            else:
                print("❌ Unknown selection.")

    def run_system(self):
        while True:
            print("\n===== 🏧 Welcome to SimpleBank ATM =====")
            print("1. Create New Account")
            print("2. Login to Account")
            print("3. Exit")

            user_input = input("Choose (1–3): ")

            if user_input == "1":
                self.open_account()
            elif user_input == "2":
                self.login_account()
            elif user_input == "3":
                print("👋 Thank you for using SimpleBank. Goodbye!")
                sys.exit()
            else:
                print("❌ Invalid selection.")


# Start ATM Simulation
if __name__ == "__main__":
    app = SimpleBankATM()
    app.run_system()