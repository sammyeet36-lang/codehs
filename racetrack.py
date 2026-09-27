# Karel runs around the racetrack 8 times, putting a ball on each corner.

# Main function: 8 laps x 4 corners = 32 corners.
def main():
    for i in range(32):
        run_to_corner()

# Karel moves to the next corner, puts down a ball, and turns to face the next side.
def run_to_corner():
    while front_is_clear():
        move()
    put_ball()
    turn_left()

main()
