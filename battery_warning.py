battery = int(input("Enter your battery percentage: "))

if battery >= 81:
    print("Fully charged!")
elif battery >= 51:
    print("You're good for now.")
elif battery >= 21:
    print("Getting low, find a charger soon.")
else:
    print("Low battery! Plug in now.")
