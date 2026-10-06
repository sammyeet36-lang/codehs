# Ask the user for their name, the movie, and how many tickets they want
name = input("Enter your name: ")
movie = input("What movie would you like to see? ")
tickets = int(input("How many tickets would you like? "))

# Print a summary of the request
print(name + " requested " + str(tickets) + " ticket(s) for " + movie + ".")
