# Determine if a student is eligible to graduate
has_enough_units = True
has_met_requirements = True

# A student can graduate only if both conditions are True
can_graduate = has_enough_units and has_met_requirements

print("Can graduate? " + str(can_graduate))
