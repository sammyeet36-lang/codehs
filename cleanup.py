# Karel sweeps the world row by row in a zigzag and picks up every tennis ball.

# Main function: clean each row, snaking up the world until the top row is done.
def main():
    clean_row()
    while left_is_clear():
        # Go up a row on the left side (now facing west) and clean it.
        turn_left()
        move()
        turn_left()
        clean_row()
        if right_is_clear():
            # Go up a row on the right side (now facing east) and clean it.
            turn_right()
            move()
            turn_right()
            clean_row()
        else:
            # Top row is done; face east so the loop ends.
            turn_around()

# Karel cleans every square in the row it is facing along.
def clean_row():
    clean_square()
    while front_is_clear():
        move()
        clean_square()

# Karel picks up all the balls on the current square.
def clean_square():
    while balls_present():
        take_ball()

main()
