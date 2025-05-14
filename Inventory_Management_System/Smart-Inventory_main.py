import sys

# Core Product Class
class StockItem:
    _global_count = 0

    def __init__(self, name, unit_price, stock_qty):
        self.name = name
        self.unit_price = unit_price
        self.stock_qty = stock_qty
        StockItem._global_count += stock_qty

    def display_info(self):
        print("\n📦 Item Information")
        print(f"Name     : {self.name}")
        print(f"Price    : {self.unit_price}")
        print(f"In Stock : {self.stock_qty}")

    def process_sale(self, qty):
        if qty <= self.stock_qty:
            self.stock_qty -= qty
            StockItem._global_count -= qty
            print(f"✅ Sold {qty} unit(s) of {self.name}")
        else:
            print("❌ Not enough stock available.")

    @staticmethod
    def get_discounted_price(price, percent):
        return round(price * (1 - percent / 100), 2)

    @classmethod
    def show_total_stock(cls):
        print(f"\n📊 Total Units in Inventory: {cls._global_count}")


# Application Logic
class InventoryManager:
    def __init__(self):
        self.catalog = []

    def register_product(self):
        print("\n🆕 Register New Product")
        name = input("Item Name: ")
        try:
            price = float(input("Unit Price ($): "))
            quantity = int(input("Stock Quantity: "))
        except ValueError:
            print("❌ Invalid input.")
            return
        self.catalog.append(StockItem(name, price, quantity))
        print(f"✅ {quantity} unit(s) of '{name}' added to inventory.")

    def list_products(self):
        print("\n📦 Product List")
        if not self.catalog:
            print("⚠️ No items available.")
            return
        for item in self.catalog:
            item.display_info()

    def handle_sale(self):
        item_name = input("Enter item name to sell: ")
        for item in self.catalog:
            if item.name.lower() == item_name.lower():
                try:
                    qty = int(input("Quantity to sell: "))
                    item.process_sale(qty)
                except ValueError:
                    print("❌ Quantity must be an integer.")
                return
        print("❌ Item not found in catalog.")

    def compute_discount(self):
        try:
            price = float(input("Enter original price: "))
            percent = float(input("Enter discount %: "))
            result = StockItem.get_discounted_price(price, percent)
            print(f"💸 Final Price after {percent}% discount: {result}")
        except ValueError:
            print("❌ Invalid numeric input.")

    def menu(self):
        options = {
            "1": self.register_product,
            "2": self.list_products,
            "3": self.handle_sale,
            "4": self.compute_discount,
            "5": StockItem.show_total_stock,
            "6": self.exit_program,
        }

        while True:
            print("\n====== 🛒 Inventory Menu ======")
            print("1. Add Item")
            print("2. View Items")
            print("3. Sell Item")
            print("4. Discount Calculator")
            print("5. View Total Stock")
            print("6. Exit")

            choice = input("Select option (1–6): ").strip()
            action = options.get(choice)

            if action:
                action()
            else:
                print("❌ Invalid choice. Try again.")

    def exit_program(self):
        print("👋 Closing Inventory Manager. Goodbye!")
        sys.exit(0)


# Launch App
if __name__ == "__main__":
    app = InventoryManager()
    app.menu()
