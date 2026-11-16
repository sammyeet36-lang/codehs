# Tests the min_to_seconds function by calling it with several different arguments.
def main():
    min_to_seconds(2)      # 120
    min_to_seconds(5)      # 300
    min_to_seconds(0)      # 0
    min_to_seconds(1.5)    # 90.0

# Takes in a number of minutes, converts it to seconds
# (there are 60 seconds in a minute), and prints the result.
def min_to_seconds(minutes):
    seconds = minutes * 60
    print(seconds)

main()
