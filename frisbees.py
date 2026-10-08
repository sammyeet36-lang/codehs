# This program calculates the total cost of buying frisbees.
# The user is asked how many frisbees they would like to buy,
# and the program prints out the total cost of their order.

# Constant for the price of one frisbee (in dollars)
COST_OF_FRISBEE = 15

# Ask the user how many frisbees they want to buy
num_frisbees = int(input("How many frisbees would you like to buy? "))

# Multiply the number of frisbees by the cost of one frisbee
total_cost = num_frisbees * COST_OF_FRISBEE

# Print the total cost for the user
print("Your total cost is $" + str(total_cost))
