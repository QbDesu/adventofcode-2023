import sys

lines = open(sys.argv[1] if len(sys.argv)>1 else "./input.txt", "r").readlines()

def find_start():
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                return (x, y)

directions = ["N", "E", "S", "W"]
direction_vectors = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}

def go_direction(pos, direction):
    return (pos[0]+direction_vectors[direction][0], pos[1]+direction_vectors[direction][1])

def get_tile(pos):
    return lines[pos[1]][pos[0]]

def is_valid_direction(pos, direction):
    tile = get_tile(pos)
    match tile:
        case "|":
            if direction in ("N", "S"):
                return True
            else:
                return False
        case "-":
            if direction in ("E", "W"):
                return True
            else:
                return False
        case "L":
            if direction in ("S", "W"):
                return True
            else:
                return False
        case "J":
            if direction in ("S", "E"):
                return True
            else:
                return False
        case "F":
            if direction in ("N", "W"):
                return True
            else:
                return False
        case "7":
            if direction in ("N", "E"):
                return True
            else:
                return False
    return False


def get_new_direction(pos, direction):
    tile = get_tile(pos)
    match tile:
        case "|":
            return direction
        case "-":
            return direction
        case "L":
            return "E" if direction=="S" else "N"
        case "J":
            return "W" if direction=="S" else "N"
        case "F":
            return "E" if direction=="N" else "S"
        case "7":
            return "W" if direction=="N" else "S"
    return None

for starting_direction in directions:
    position = find_start()
    direction = starting_direction

    steps = 0
    while True:
        position = go_direction(position, direction)
        steps += 1

        tile = get_tile(position)
        if tile == "S":
            print(f"Found loop going {starting_direction}!")
            print(f"Steps: {steps}, furthest point: {steps//2}")
            break
        if tile == ".":
            print(f"Found break going {starting_direction}!")
            break
        else:
            if not is_valid_direction(position, direction):
                print(f"Found invalid direction going {starting_direction}!")
                break
            direction = get_new_direction(position, direction)
