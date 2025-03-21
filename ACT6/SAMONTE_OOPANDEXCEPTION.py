class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"Item(ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: {self.price})"


class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        if item_id in self.items:
            raise ValueError("Item ID already exists.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        item = Item(item_id, name, description, price)
        self.items[item_id] = item
        return item

    def read_item(self, item_id):
        if item_id not in self.items:
            raise KeyError("Item not found.")
        return self.items[item_id]

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            raise KeyError("Item not found.")
        
        item = self.items[item_id]
        if name is not None:
            item.name = name
        if description is not None:
            item.description = description
        if price is not None:
            if price < 0:
                raise ValueError("Price cannot be negative.")
            item.price = price
        return item

    def delete_item(self, item_id):
        if item_id not in self.items:
            raise KeyError("Item not found.")
        del self.items[item_id]

    def list_items(self):
        return list(self.items.values())


def main():
    manager = ItemManager()

    while True:
        print("\nItem Management Application")
        print("1. Create Item")
        print("2. Read Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. List Items")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == '1':
                item_id = input("Enter item ID: ")
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                item = manager.create_item(item_id, name, description, price)
                print(f"Created: {item}")

            elif choice == '2':
                item_id = input("Enter item ID to read: ")
                item = manager.read_item(item_id)
                print(item)

            elif choice == '3':
                item_id = input("Enter item ID to update: ")
                name = input("Enter new item name (leave blank to keep current): ")
                description = input("Enter new item description (leave blank to keep current): ")
                price_input = input("Enter new item price (leave blank to keep current): ")
                price = float(price_input) if price_input else None
                item = manager.update_item(item_id, name if name else None, description if description else None, price)
                print(f"Updated: {item}")

            elif choice == '4':
                item_id = input("Enter item ID to delete: ")
                manager.delete_item(item_id)
                print("Item deleted.")

            elif choice == '5':
                items = manager.list_items()
                for item in items:
                    print(item)

            elif choice == '6':
                print("Exiting the application.")
                break

            else:
                print("Invalid choice. Please try again.")

        except (ValueError, KeyError) as e:
            print(f"Error: {e}")



main()