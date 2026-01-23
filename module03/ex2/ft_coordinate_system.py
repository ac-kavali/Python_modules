import sys
import math


def calculate_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance


def parse_coordinates(arg, coords):
    try:
        numbers_str = arg.split("(")[1].split(")")[0]  #this called chained method calls
        numbers_list = numbers_str.split(", ")
        coords = tuple(int(x) for x in numbers_list)
        return coords
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: {type(e).__name__} Args: ("{e}")')
        return coords

def unpacking_demonstration(latest_coords):
    print("\nUnpacking demonstration:")
    x, y, z = latest_coords
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")



coordinates = initial_position = (0, 0, 0)

# parsing the coordinates giving in command line
coordinates = parse_coordinates(sys.argv[1], coordinates)
print("=== Game Coordinate System ===")
print(f"\nPosition created: {coordinates}")
print(
    f"Distance between {initial_position} "
    f"and {coordinates}: "
    f"{calculate_distance(initial_position, coordinates):.1f}"
)

#parsing new input coordinates and calculate distance
coordinates = parse_coordinates(input("\nParsing coordinates:"), coordinates)
print(f"Parsed position: {coordinates}")
print(
    f"Distance between {initial_position} "
    f"and {coordinates}: "
    f"{calculate_distance(initial_position, coordinates):.1f}"
)


print('\nParsing invalid coordinates: "abc,def,ghi"')
coordinates = parse_coordinates("(aa, bb, cc)", coordinates)

#unpacking the demonstration
unpacking_demonstration(coordinates)