import sys
import math


def calculate_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance


def parse_coordinates(arg):
    try:
        numbers_str = arg.split("(")[1].split(")")[0] #this called chained method calls
        print(numbers_str)
        numbers_list = numbers_str.split(", ")
        print(numbers_list)
        coords = tuple(int(x) for x in numbers_list)
        return coords
    except ValueError as e:
        print(e)

initial_position = (0, 0, 0)
coordinates1 = parse_coordinates(sys.argv[1])



print('Parsing invalid coordinates: "abc,def,ghi"')
parse_coordinates(sys.argv[1])
