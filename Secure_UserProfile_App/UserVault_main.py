import re

# Data model for each user
class AccountProfile:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = None
        self.update_password(password)

    def update_email(self, new_email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            self._email = new_email
            print("✅ Email updated.")
        else:
            print("❌ Invalid email format.")

    def update_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
            print("🔐 Password set.")
        else:
            print("❌ Password must be at least 6 characters.")

    def masked_password(self):
        return "*" * len(self.__password) if self.__password else "No password"

    def show_details(self):
        print("\n📄 User Information")
        print(f"Username: {self.username}")
        print(f"Email: {self._email}")
        print(f"Password: {self.masked_password()}")


# Main application logic
class UserVaultApp:
    def __init__(self):
        self._user_list = []

    def add_user(self):
        print("\n🔧 Create New User")
        username = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")
        user = AccountProfile(username, email, password)
        self._user_list.append(user)
        print("✅ User profile created.")

    def show_all_users(self):
        if not self._user_list:
            print("⚠️ No user profiles available.")
            return
        for user in self._user_list:
            user.show_details()

    def modify_email(self):
        name = input("Enter the username to modify email: ")
        for user in self._user_list:
            if user.username == name:
                new_email = input("Enter new email address: ")
                user.update_email(new_email)
                return
        print("❌ User not found.")

    def run(self):
        while True:
            print("\n===== 🛡️ Secure UserVault Menu =====")
            print("1. Register New User")
            print("2. View User Profiles")
            print("3. Update Email Address")
            print("4. Exit")

            option = input("Choose an option (1–4): ").strip()

            if option == '1':
                self.add_user()
            elif option == '2':
                self.show_all_users()
            elif option == '3':
                self.modify_email()
            elif option == '4':
                print("👋 Exiting... Stay secure!")
                break
            else:
                print("❌ Invalid option. Try again.")

# Launch the app
if __name__ == "__main__":
    app = UserVaultApp()
    app.run()