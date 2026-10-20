# Determine whether you have school today
is_weekday = True
is_holiday = False

# School happens on a weekday that is not a holiday
have_school_today = is_weekday and not is_holiday

print("You have school today: " + str(have_school_today))
