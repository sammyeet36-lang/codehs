# This program helps the user figure out how much to pay at a restaurant.
# The user is asked for the bill amount and the tip percentage they want
# to leave, and the program prints the bill, the tip, and the total.

# Ask the user for the bill amount
bill = float(input("What is the bill amount? "))

# Ask the user what tip percentage they would like to leave
tip_percent = float(input("What tip percentage would you like to leave? "))

# Calculate the tip amount and the total bill
tip = bill * tip_percent / 100
total = bill + tip

# Print the bill, the tip, and the total
print("The bill is " + str(bill) + " and the tip is " + str(tip) + ", bringing the total to " + str(total))
