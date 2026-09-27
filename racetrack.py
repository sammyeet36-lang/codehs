# Racetrack Karel
# Karel runs around the racetrack eight times and ends back at the
# starting spot. Every time Karel reaches a corner, Karel puts down a
# ball, so at the end there are 8 balls on each corner.
# This works on any size racetrack because Karel moves until the front
# is blocked instead of counting a fixed number of steps.


# Main function: Karel runs 8 laps around the racetrack.
def main():
    for i in range(8):
        run_lap()


# Karel runs one full lap by running all 4 sides of the track.
# Precondition: Karel is on a corner, facing along the track.
# Postcondition: Karel is back on the same corner, facing the same way,
# with one more ball on every corner.
def run_lap():
    for i in range(4):
        run_side()


# Karel runs down one side of the track to the next corner,
# drops a ball on that corner, and turns to face the next side.
# Precondition: Karel is facing along a side of the track.
# Postcondition: Karel is on the next corner, facing the next side.
def run_side():
    move_to_wall()
    put_ball()
    turn_left()


# Karel moves forward until there is a wall in front.
# Precondition: none.
# Postcondition: Karel's front is blocked.
def move_to_wall():
    while front_is_clear():
        move()


main()
