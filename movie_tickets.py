tickets = int(input("How many tickets did you buy? "))

if tickets >= 4:
    print("You get free popcorn.")
    if tickets >= 6:
        print("You get free soda.")
else:
    print("No free popcorn.")
