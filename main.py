# Prompt the user for input and convert to appropriate data types
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity: "))

# Calculate the total cost
total = price * quantity

# Display the friendly summary using an f-string
print(f"{quantity} items at {price:.2f} each = {total:.2f}")

