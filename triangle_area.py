# Tests the triangle_area function by calling it with several different
# bases and heights.
def main():
    triangle_area(5, 4)     # 10.0
    triangle_area(6, 3)     # 9.0
    triangle_area(7, 2)     # 7.0
    triangle_area(3, 5)     # 7.5

# Takes in the base and height of a triangle, computes its area
# using the formula 1/2 * base * height, and prints the result.
def triangle_area(base, height):
    area = 1/2 * base * height
    print(area)

main()
