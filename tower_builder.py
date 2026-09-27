# Karel builds a tower of 3 balls on every odd column in the world.

# Main function: build a tower, then skip a column and build again until the wall.
def main():
    build_tower()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            build_tower()

# Karel builds a 3-ball tower going up, then comes back down facing east.
def build_tower():
    turn_left()
    put_ball()
    move()
    put_ball()
    move()
    put_ball()
    turn_around()
    move()
    move()
    turn_left()

main()
