import sys

# Product Base Class
class Product:
    _total_inventory = 0

    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity
        Product._total_inventory += quantity

    def show_details(self):
        print("\n📦 Product Details")
        print(f"📝 Name     : {self.title}")
        print(f"💵 Price    : {self.price}")
        print(f"📦 In Stock : {self.quantity}")

    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            Product._total_inventory -= amount
            print(f"✅ {amount} unit(s) of '{self.title}' sold.")
        else:
            print("⚠️ Insufficient stock available.")

    @staticmethod
    def apply_discount(original_price, discount_percent):
        return round(original_price * (1 - discount_percent / 100), 2)

    @classmethod
    def display_total_inventory(cls):
        print(f"\n📊 Total Items in Inventory: {cls._total_inventory}")


# Inventory Controller
class Warehouse:
    def __init__(self):
        self.items = []

    def add_new_product(self):
        print("\n➕ Add New Product")
        name = input("Enter product name: ").strip()
        try:
            cost = float(input("Enter unit price: ").strip())
            stock = int(input("Enter quantity in stock: ").strip())
        except ValueError:
            print("❌ Invalid number format.")
            return

        self.items.append(Product(name, cost, stock))
        print(f"✅ '{name}' ({stock} units) added to warehouse.")

    def show_all_products(self):
        print("\n📋 Current Product List")
        if not self.items:
            print("📭 No products in the warehouse.")
            return
        for p in self.items:
            p.show_details()

    def process_transaction(self):
        search_name = input("Enter product to sell: ").strip()
        for p in self.items:
            if p.title.lower() == search_name.lower():
                try:
                    amount = int(input("Quantity to sell: ").strip())
                    p.sell(amount)
                except ValueError:
                    print("❌ Please enter a valid number.")
                return
        print("🔍 Product not found in inventory.")

    def calculate_discount(self):
        try:
            original = float(input("Original price: ").strip())
            discount = float(input("Discount percentage: ").strip())
            final = Product.apply_discount(original, discount)
            print(f"💰 Final price after {discount}% off: {final}")
        except ValueError:
            print("❌ Invalid input.")

    def run_menu(self):
        choices = {
            "1": self.add_new_product,
            "2": self.show_all_products,
            "3": self.process_transaction,
            "4": self.calculate_discount,
            "5": Product.display_total_inventory,
            "6": self.quit_app,
        }

        while True:
            print("\n====== 🧮 Warehouse Console ======")
            print("1. Add New Product")
            print("2. List All Products")
            print("3. Sell a Product")
            print("4. Discount Tool")
            print("5. View Inventory Summary")
            print("6. Exit")

            user_input = input("Your choice (1–6): ").strip()
            selected = choices.get(user_input)
            if selected:
                selected()
            else:
                print("❌ Unknown option. Please choose again.")

    def quit_app(self):
        print("👋 Exiting Warehouse System. See you soon!")
        sys.exit()


# Start Program
if __name__ == "__main__":
    system = Warehouse()
    system.run_menu()
