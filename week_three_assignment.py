# Assignment: Discount Calculator

# 1. Create a function that calculates discount
def calculate_discount(price, discount_percent):
    # Check if discount is 20% or more
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * discount_percent / 100
        # Calculate final price
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# 2. Get input from user and use the function
print("Welcome to the Discount Calculator!")

# Get the original price from user
price = float(input("Enter the original price: $"))

# Get the discount percentage from user
discount_percent = float(input("Enter the discount percentage: "))

# Call the function to calculate final price
final_price = calculate_discount(price, discount_percent)

# Print the results
print(f"Original price: ${price}")
print(f"Discount: {discount_percent}%")

# Check if discount was applied
if discount_percent >= 20:
    print(f"Final price: ${final_price}")
else:
    print(f"No discount applied. Price remains: ${final_price}")