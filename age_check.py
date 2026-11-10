# Loop and a half: ask for an age until it is between 0 and 120
while True:
    age = int(input("Enter your age: "))
    if age >= 0 and age <= 120:
        print("Thank you! Your age is valid.")
        break
    print("That is not a valid age. Please try again.")
