import sys
import math


def calculate_distance(p1, p2):
    """This function unpack the two coordinates tuples and
    use the formula to calculate the distance"""
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    distance = math.sqrt(
        (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    )
    return distance


def parse_coordinates(arg, coords):
    """This function parse the argument and except the ValueError
    if occurred and avoid old coordinates to be corrupted"""
    try:
        numbers = arg.split("(")[1].split(")")[0]
        numbers = numbers.split(", ")
        coords = tuple(int(x) for x in numbers)
        return coords
    except (ValueError, KeyError) as e:
        print(f"Error parsing coordinates: {e}")
        print(
            f'Error details - Type: {type(e).__name__} '
            f'Args: ("{e}")'
        )
        return coords


def unpacking_demonstration(latest_coords):
    print("\nUnpacking demonstration:")
    x, y, z = latest_coords
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


coordinates = initial_position = (0, 0, 0)

# Parsing the coordinates given in command line
coordinates = parse_coordinates(sys.argv[1], coordinates)
print("=== Game Coordinate System ===")
print(f"\nPosition created: {coordinates}")
print(
    f"Distance between {initial_position} "
    f"and {coordinates}: "
    f"{calculate_distance(initial_position, coordinates):.1f}"
)

# Parsing new input coordinates and calculate distance
coordinates = parse_coordinates(input("\nParsing coordinates:"), coordinates)
print(f"Parsed position: {coordinates}")
print(
    f"Distance between {initial_position} "
    f"and {coordinates}: "
    f"{calculate_distance(initial_position, coordinates):.1f}"
)

print('\nParsing invalid coordinates: "abc,def,ghi"')
coordinates = parse_coordinates("(aa, bb, cc)", coordinates)

# Unpacking demonstration
unpacking_demonstration(coordinates)
