# Base class: Employee
class Employee:
    def __init__(self, name, eid, salary):
        self.name = name
        self.eid = eid
        self.salary = salary

    def display_info(self):
        print("\n📄 [EMPLOYEE RECORD]")
        print(f"👨‍💼 Name       : {self.name}")
        print(f"🆔 Employee ID : {self.eid}")
        print(f"💵 Base Salary : ${self.salary:.2f}")

    def calc_bonus(self):
        return self.salary * 0.1


# Subclass: Manager
class Manager(Employee):
    def __init__(self, name, eid, salary, department):
        super().__init__(name, eid, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"🏬 Department  : {self.department}")

    def calc_bonus(self):
        return self.salary * 0.2


# Subclass: Developer
class Developer(Employee):
    def __init__(self, name, eid, salary, skills):
        super().__init__(name, eid, salary)
        self.skills = skills

    def display_info(self):
        super().display_info()
        print(f"🧑‍💻 Skills     : {self.skills}")

    def calc_bonus(self):
        return self.salary * 0.5


# Database of Employees
company_employees = []


# Function: Add Employee
def add_employee():
    print("\n--- Add New Team Member ---")
    print("1. General Staff")
    print("2. Manager")
    print("3. Developer")

    try:
        role = int(input("Select role (1–3): "))
    except ValueError:
        print("❌ Input must be a number.")
        return

    name = input("Full Name: ").strip()
    emp_id = input("Employee ID: ").strip()

    try:
        pay = float(input("Base Salary: $"))
    except ValueError:
        print("❌ Invalid salary amount.")
        return

    if role == 1:
        company_employees.append(Employee(name, emp_id, pay))
    elif role == 2:
        dept = input("Department: ").strip()
        company_employees.append(Manager(name, emp_id, pay, dept))
    elif role == 3:
        stack = input("Technical Skills: ").strip()
        company_employees.append(Developer(name, emp_id, pay, stack))
    else:
        print("⚠️ Invalid role selected.")


# Function: Show all employees
def show_employees():
    if not company_employees:
        print("📂 No records found.")
        return

    print("\n=== TEAM DIRECTORY ===")
    for emp in company_employees:
        emp.display_info()
        print(f"🎉 Bonus       : ${emp.calc_bonus():.2f}")
        print("-" * 32)


# Application Loop
def launch_console():
    while True:
        print("\n======== HR MANAGEMENT SYSTEM ========")
        print("1. Add New Employee")
        print("2. List All Employees")
        print("3. Exit Program")

        try:
            choice = int(input("Your choice (1–3): "))
        except ValueError:
            print("❌ Please input a valid option.")
            continue

        if choice == 1:
            add_employee()
        elif choice == 2:
            show_employees()
        elif choice == 3:
            print("✅ System shutdown. Thank you!")
            break
        else:
            print("🚫 Invalid selection. Try again.")


# Start the program
launch_console()
