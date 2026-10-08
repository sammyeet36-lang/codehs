# Ask the user for the total number of minutes
total_minutes = int(input("Enter minutes: "))

# Calculate full hours and remaining minutes
hours = total_minutes // 60
minutes = total_minutes % 60

# Print the result
print(str(total_minutes) + " minutes is " + str(hours) + " hours and " + str(minutes) + " minutes.")
