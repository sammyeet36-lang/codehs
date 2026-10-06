# Ask the user for their name, the item they want, and how many
name = input("Enter your name: ")
item = input("What item would you like to request? ")
quantity = int(input("How many would you like? "))

# Drop a trailing "s" so "Notebooks" becomes "Notebook(s)"
if item.endswith("s"):
    item = item[:-1]

# Print a summary of the request
print(name + " requested " + str(quantity) + " " + item + "(s).")
