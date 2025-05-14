# Base class: Staff
class Staff:
    def __init__(self, fullname, staff_id, base_pay):
        self.fullname = fullname
        self.staff_id = staff_id
        self.base_pay = base_pay

    def show_profile(self):
        print("\n📌 Employee Profile")
        print(f"👤 Name       : {self.fullname}")
        print(f"🆔 ID         : {self.staff_id}")
        print(f"💰 Salary     : {self.base_pay}")

    def get_bonus(self):
        return self.base_pay * 0.1


# Derived class: Supervisor
class Supervisor(Staff):
    def __init__(self, fullname, staff_id, base_pay, division):
        super().__init__(fullname, staff_id, base_pay)
        self.division = division

    def show_profile(self):
        super().show_profile()
        print(f"🏢 Division   : {self.division}")

    def get_bonus(self):
        return self.base_pay * 0.2


# Derived class: Engineer
class Engineer(Staff):
    def __init__(self, fullname, staff_id, base_pay, tech_stack):
        super().__init__(fullname, staff_id, base_pay)
        self.tech_stack = tech_stack

    def show_profile(self):
        super().show_profile()
        print(f"💻 Tech Stack : {self.tech_stack}")

    def get_bonus(self):
        return self.base_pay * 0.5


# Global staff list
team_roster = []


# Add new staff member
def register_employee():
    print("\n=== Add New Employee ===")
    print("1. Staff")
    print("2. Supervisor")
    print("3. Engineer")

    try:
        option = int(input("Select role type (1–3): ").strip())
    except ValueError:
        print("❌ Invalid input.")
        return

    fullname = input("Enter full name: ").strip()
    staff_id = input("Enter ID: ").strip()
    try:
        salary = float(input("Enter base salary ($): ").strip())
    except ValueError:
        print("❌ Invalid salary input.")
        return

    if option == 1:
        team_roster.append(Staff(fullname, staff_id, salary))
    elif option == 2:
        division = input("Enter division: ").strip()
        team_roster.append(Supervisor(fullname, staff_id, salary, division))
    elif option == 3:
        tech_stack = input("Enter tech stack: ").strip()
        team_roster.append(Engineer(fullname, staff_id, salary, tech_stack))
    else:
        print("❌ Invalid role selection.")


# Display all employees
def view_all_employees():
    if not team_roster:
        print("📭 No employees registered.")
        return

    print("\n=== Company Roster ===")
    for member in team_roster:
        member.show_profile()
        print(f"🎁 Bonus      : {member.get_bonus()}")
        print("-" * 30)


# Main interactive loop
def run_console():
    while True:
        print("\n===== EMPLOYEE MANAGEMENT CONSOLE =====")
        print("1. Register Employee")
        print("2. View All Employees")
        print("3. Exit")

        try:
            task = int(input("Choose an option (1–3): ").strip())
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if task == 1:
            register_employee()
        elif task == 2:
            view_all_employees()
        elif task == 3:
            print("👋 Program closed. Goodbye!")
            break
        else:
            print("❗ Invalid option selected.")


# Run the application
run_console()