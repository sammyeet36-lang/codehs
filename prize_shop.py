# Name: Your Name Here
# This program decides which prize a customer earns at the Prize Shop
# based on their age and the number of tickets they earned.

# Ask the customer for their information and store each answer.
name = input("What is your name? ")
age = int(input("How old are you? "))
tickets = int(input("How many tickets did you earn? "))

# Boolean: True if the customer is at least 13, False otherwise.
is_old_enough = age >= 13
print("Age requirement met: " + str(is_old_enough))

# Decide which prize the customer earns.
if tickets >= 100 and is_old_enough:
    print("Congratulations! You earned Headphones!")
elif tickets >= 50 or is_old_enough:
    print("Congratulations! You earned a Candy Bag!")
else:
    print("You earned a Sticker. Keep collecting tickets!")

# Repeat the welcome message three times.
for i in range(3):
    print("Thanks for visiting the Prize Shop!")
