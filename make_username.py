# Tests the make_username function by calling it with several different names.
def main():
    make_username("maria")     # maria_student
    make_username("james")     # james_student
    make_username("aisha")     # aisha_student

# Takes in a first name, adds "_student" to the end of it,
# and prints the resulting username.
def make_username(first_name):
    username = first_name + "_student"
    print(username)

main()
