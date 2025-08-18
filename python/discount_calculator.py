# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Prompt user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call function and print result
final_price = calculate_discount(price, discount_percent)
print("Final price after discount:", final_price)
