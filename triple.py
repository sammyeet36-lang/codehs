# Tests the triple function by calling it with several different arguments.
def main():
    triple(4)      # 12
    triple(5)      # 15
    triple(0)      # 0
    triple(-2)     # -6
    triple(1.5)    # 4.5

# Takes in a number x, triples it (multiplies it by 3),
# and prints the result.
def triple(x):
    result = x * 3
    print(result)

main()
