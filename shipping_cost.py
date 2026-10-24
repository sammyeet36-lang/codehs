weight = float(input("Enter package weight in pounds: "))

if weight < 1:
    print("Shipping cost: $3.99")
elif weight < 5:
    print("Shipping cost: $7.99")
elif weight < 10:
    print("Shipping cost: $12.99")
else:
    print("Shipping cost: $19.99")
