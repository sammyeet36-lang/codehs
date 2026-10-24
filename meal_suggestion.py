meal = input("Which meal is it? (breakfast, lunch, or dinner): ").lower()

if meal == "breakfast":
    print("How about some avocado on toast?")
elif meal == "lunch":
    print("How about a turkey sandwich with a side salad?")
elif meal == "dinner":
    print("How about spaghetti and meatballs?")
else:
    print("Sorry, that is not a valid option.")
