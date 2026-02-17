"""
Restaurant Menu Management
Add, remove and check food items
"""

def add_item(menu: list, item: str):
    menu.append(item)

def remove_item(menu: list, item: str):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found in menu")

def check_item(menu: list, item: str):
    if item in menu:
        print(f"{item} is available")
    else:
        print(f"{item} is not available")


# Example Run
if __name__ == "__main__":
    initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]

    add_item(initial_menu, "Tacos")
    remove_item(initial_menu, "Salad")
    check_item(initial_menu, "Pizza")

    print("Updated menu:", initial_menu)
