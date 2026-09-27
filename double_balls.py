# Karel doubles the pile of balls on 1st street, 2nd avenue.

# Main function: double the pile into the next spot, bring it back, then go home.
def main():
    move()
    double_pile()
    move_pile_back()
    turn_around()
    move()
    move()
    turn_around()

# For every ball in the pile, Karel puts 2 balls one spot to the east.
# Ends on the (now empty) pile spot facing east.
def double_pile():
    while balls_present():
        take_ball()
        move()
        put_ball()
        put_ball()
        turn_around()
        move()
        turn_around()

# Karel moves every ball from the spot to the east back onto the pile spot.
# Ends on the (now empty) spot east of the pile, facing east.
def move_pile_back():
    move()
    while balls_present():
        take_ball()
        turn_around()
        move()
        put_ball()
        turn_around()
        move()

main()
