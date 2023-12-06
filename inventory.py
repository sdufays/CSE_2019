import os

# Class definition for Item
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.info = f'{name} (Quantity: {quantity} / Price: ${price})'

# Function to convert list to string
def list_to_string(lst):
    return ''.join(lst)

# Function to add an item
def add_item():
    with open("list_items.txt", "a") as item_file, open("inventory.txt", "a") as inventory_file:
        name = input("Item name: ")
        price = input("Item price: ")
        quantity = input("Item quantity: ")

        new_item = Item(name, price, quantity)
        item_file.write(f"{new_item.name}\n")
        inventory_file.write(f"{new_item.info}\n")

    print_current_items()

# Function to remove an item
def remove_item():
    target_item = input("Item to remove: ")
    update_file("inventory.txt", target_item)
    update_file("list_items.txt", target_item)

# Function to update a file by removing a specific line
def update_file(filename, target_line):
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            if target_line not in line:
                file.write(line)

# Function to print current items
def print_current_items():
    with open("list_items.txt", "r") as file:
        items = file.readlines()
    print("Current items in inventory:\n" + list_to_string(items))

# Function to generate a report
def generate_report():
    with open("list_items.txt", "r") as file:
        items = file.readlines()
    print("Weekly Report:\n" + list_to_string(items))

# Function to view inventory
def view_inventory():
    with open("inventory.txt", "r") as file:
        inventory = file.readlines()
    print(list_to_string(inventory))

# Function to record a sale
def record_sale():
    print_current_items()
    item_to_sell = input("Item to record a sale for:\n")
    # Additional functionality to record a sale can be added here

# Import ConsoleMenu and related classes
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem, SubmenuItem, SelectionMenu

# Create the menu
menu = ConsoleMenu("Inventory Management System", "Welcome!")

# Adding menu items
menu.append_item(FunctionItem("Add Items to Inventory", add_item))
menu.append_item(FunctionItem("Remove Items from Inventory", remove_item))
menu.append_item(FunctionItem("Generate Weekly Report", generate_report))
menu.append_item(FunctionItem("View Inventory", view_inventory))
menu.append_item(FunctionItem("Record a Sale", record_sale))

# Submenu for days of the week
days_of_week_menu = SelectionMenu(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "Days of the Week")
menu.append_item(SubmenuItem("Days of the Week", days_of_week_menu, menu))

# Display the menu
menu.show()
