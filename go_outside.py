# Determine whether you can go outside based on the weather
is_free_time = True
is_windy = False
is_raining = True
has_umbrella = True

# Need free time, no wind, and either no rain or an umbrella
can_go_outside = is_free_time and not is_windy and (not is_raining or has_umbrella)

print("Can go outside: " + str(can_go_outside))
