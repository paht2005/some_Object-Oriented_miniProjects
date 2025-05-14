class Publication:
    def __init__(self, name, writer):
        self.name = name
        self.writer = writer
        self.is_checked_out = False

    def show_details(self):
        availability = "In Library" if not self.is_checked_out else "On Loan"
        print(f"Book Title : {self.name}")
        print(f"Written By: {self.writer}")
        print(f"Status    : {availability}\n")


class Archive:
    def __init__(self):
        self.collection = []

    def insert_book(self, name, writer):
        item = Publication(name, writer)2
        self.collection.append(item)
        print(f"'{name}' by {writer} has been cataloged.")

    def list_books(self):
        if not self.collection:
            print("Library has no books at the moment.")
        else:
            print("\n📚 Library Inventory 📚")
            for doc in self.collection:
                doc.show_details()

    def checkout(self, book_name):
        for doc in self.collection:
            if doc.name.lower() == book_name.lower() and not doc.is_checked_out:
                doc.is_checked_out = True
                print(f"You've borrowed '{doc.name}'. Please return on time!")
                return
        print(f"'{book_name}' is not available or already borrowed.")

    def checkin(self, book_name):
        for doc in self.collection:
            if doc.name.lower() == book_name.lower() and doc.is_checked_out:
                doc.is_checked_out = False
                print(f"Thank you for returning '{doc.name}'.")
                return
        print(f"No matching record for '{book_name}' being borrowed.")


# App Controller
def run_library_app():
    system = Archive()

    while True:
        print("\n==== Book System Console ====")
        print("1. Register New Book")
        print("2. Show Book List")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Quit")

        action = input("Select an option (1-5): ").strip()

        if action == "1":
            name = input("Enter the book's title: ").strip()
            writer = input("Enter the author's name: ").strip()
            system.insert_book(name, writer)

        elif action == "2":
            system.list_books()

        elif action == "3":
            name = input("Which book would you like to borrow? ").strip()
            system.checkout(name)

        elif action == "4":
            name = input("Which book are you returning? ").strip()
            system.checkin(name)

        elif action == "5":
            print("👋 Exiting Book System. Come again soon!")
            break

        else:
            print("Invalid choice. Please choose between 1 and 5.")

# Start App
run_library_app()
