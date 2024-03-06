TAX_RATE = 0.08  # 8% tax rate
DISCOUNT_PERCENTAGE = 0.1  # 10% discount

def calculate_total_cost(price, quantity):
    subtotal = price * quantity # Calculate the subtotal
    tax_amount = subtotal * TAX_RATE # Calculate the tax amount
    discount_amount = subtotal * DISCOUNT_PERCENTAGE # Calculate the discount amount
    total_cost = subtotal + tax_amount - discount_amount # Calculate the total cost
    return total_cost # Return the total cost

print(calculate_total_cost(10, 2))  # Expected output: 19.6 (with tax and discount applied)
print(calculate_total_cost(15, 3))  # Expected output: 44.1
print(calculate_total_cost(20, 1))  # Expected output: 19.6