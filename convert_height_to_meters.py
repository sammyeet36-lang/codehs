INCHES_TO_CM = 2.54
CM_TO_METERS = 0.01
FEET_TO_INCHES = 12

# Tests the convert_height_to_meters function with several different heights.
def main():
    convert_height_to_meters(6, 4)
    convert_height_to_meters(5, 8)
    convert_height_to_meters(5, 2)

# Takes in a height in feet and inches, converts it to meters,
# and prints the result.
# How the conversion works:
#   1. There are 12 inches in a foot (FEET_TO_INCHES),
#      so total inches = feet * 12 + inches.
#   2. There are 2.54 centimeters in an inch (INCHES_TO_CM),
#      so centimeters = total inches * 2.54.
#   3. There are 100 centimeters in a meter, so multiplying by
#      0.01 (CM_TO_METERS) is the same as dividing by 100.
def convert_height_to_meters(feet, inches):
    total_inches = (feet * FEET_TO_INCHES) + inches
    centimeters = total_inches * INCHES_TO_CM
    meters = centimeters * CM_TO_METERS
    # Round to 4 decimal places to remove tiny computer rounding errors
    meters = round(meters, 4)
    print(str(feet) + " feet, " + str(inches) + " inches = " + str(meters) + " meters")

main()
