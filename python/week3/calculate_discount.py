def calculate_discount(cost, off_percent):
    # Only apply discount if it's 20% or above
    return cost * (1 - off_percent / 100) if off_percent >= 20 else cost

# Collect user input
item_price = float(input("Please type in the price of the product: "))
offer = float(input("How much percent discount is given? "))

new_price = calculate_discount(item_price, offer)

# Print in a unique style
if offer >= 20:
    print(f"Congrats! You got {offer}% off. You now pay ₦{new_price:.2f}")
else:
    print(f"No big discount applied. The price stays at ₦{new_price:.2f}")
