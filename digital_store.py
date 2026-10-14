# Store information
store_name = "Page Turner Books"
sales_tax_rate = 0.08

# Welcome message
print("Welcome to " + store_name + "!")

# Customer information
customer_name = input("What is your name? ")

# Product information
product = input("What book would you like to buy? ")
price_text = input("What is the price? ")
price = float(price_text.replace("$", "").strip())
quantity = int(input("How many would you like? "))

# Calculations
subtotal = price * quantity
sales_tax = subtotal * sales_tax_rate
final_total = subtotal + sales_tax

# Receipt
print("")
print("------------------------------")
print("      " + store_name.upper())
print("------------------------------")
print("Customer: " + customer_name)
print("Product: " + product)
print("Price: $" + format(price, ".2f"))
print("Quantity: " + str(quantity))
print("Subtotal: $" + format(subtotal, ".2f"))
print("Sales Tax: $" + format(sales_tax, ".2f"))
print("Total: $" + format(final_total, ".2f"))
print("------------------------------")

# Thank-you message
print("Thank you, " + customer_name + "!")
