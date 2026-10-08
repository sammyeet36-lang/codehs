# This program calculates how fast the user ran in miles per hour.
# The user is asked how many miles they ran and how many minutes
# it took them, and the program prints out their speed in mph.

# Ask the user how many miles they ran
miles = float(input("How many miles did you run? "))

# Ask the user how many minutes it took them
minutes = float(input("How many minutes did it take you? "))

# Convert minutes to hours, then divide miles by hours to get mph
hours = minutes / 60
speed = miles / hours

# Print the user's speed in miles per hour
print("Speed in mph: " + str(speed))
