import random

# Shake the Magic 8 Ball: pick a random number from 1 to 4
number = random.randint(1, 4)

# Print exactly one response based on the number
if number == 1:
    print("Yes, definitely.")
elif number == 2:
    print("Ask again later.")
elif number == 3:
    print("Outlook not so good.")
else:
    print("It is certain.")
