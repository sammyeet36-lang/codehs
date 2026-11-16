# Tests the convert_height_to_meters function with several different heights.
def main():
    convert_height_to_meters(6, 4)
    convert_height_to_meters(5, 8)
    convert_height_to_meters(5, 2)

# Takes in a height in feet and inches, converts it to meters,
# and prints the result.
# How the conversion works:
#   1. There are 12 inches in a foot, so total inches = feet * 12 + inches.
#   2. There are 2.54 centimeters in an inch, so centimeters = total inches * 2.54.
#   3. There are 100 centimeters in a meter, so meters = centimeters / 100.
def convert_height_to_meters(feet, inches):
    total_inches = (feet * 12) + inches
    centimeters = total_inches * 2.54
    meters = centimeters / 100
    # Round to 4 decimal places to remove tiny computer rounding errors
    meters = round(meters, 4)
    print(str(feet) + " feet, " + str(inches) + " inches = " + str(meters) + " meters")

main()
