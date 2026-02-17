"""
E-Commerce Cart System
Calculates total cart price and applies 10% discount if more than 5 items
"""

def calculate_total(cart_items: dict) -> float:
    if not cart_items:
        return 0

    total = sum(cart_items.values())

    # discount
    if len(cart_items) > 5:
        total *= 0.9

    return total


# Example Run
if __name__ == "__main__":
    cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}

    total_price = calculate_total(cart_items)

    if total_price == 0:
        print("Cart is empty")
    else:
        print(f"Total Price: {total_price:.0f}")
