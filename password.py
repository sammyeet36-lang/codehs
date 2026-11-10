SECRET = "abc123"

# Loop and a half: ask for the password until it matches
while True:
    password = input("Enter password: ")
    if password == SECRET:
        print("You got it!")
        break
    print("Sorry, that did not match. Please try again.")
