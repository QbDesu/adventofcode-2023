import sys

lines = open(sys.argv[1] if len(sys.argv) >
             1 else "./input.txt", "r").readlines()


def find_start():
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                return (x, y)

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


def set_tile(pos, value):
    x, y = pos
    line = lines[y]
    lines[y] = line[:x] + value + line[x+1:]


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
            return "E" if direction == "S" else "N"
        case "J":
            return "W" if direction == "S" else "N"
        case "F":
            return "E" if direction == "N" else "S"
        case "7":
            return "W" if direction == "N" else "S"
    return None

def invert_direction(direction):
    if direction == "N":
        return "S"
    elif direction == "E":
        return "W"
    elif direction == "S":
        return "N"
    elif direction == "W":
        return "E"

def get_tile_from_directions(a, b):
    tupled = tuple(sorted((a, b)))
    match tupled:
        case ("E", "N"):
            return "L"
        case ("E", "S"):
            return "F"
        case ("E", "W"):
            return "-"
        case ("N", "S"):
            return "|"
        case ("N", "W"):
            return "J"
        case ("S", "W"):
            return "7"

def get_loop():
    starting_position = find_start()
    print(f"Starting at {starting_position}")

    for starting_direction in ("N", "E", "S"):
        position = starting_position
        direction = starting_direction

        loop = []

        while True:
            position = go_direction(position, direction)
            loop.append(position)

            tile = get_tile(position)
            if tile == "S":
                print(f"Found loop going {starting_direction}!")
                set_tile(position, get_tile_from_directions(starting_direction, invert_direction(direction)))
                return loop
            if tile == ".":
                print(f"Found break going {starting_direction}!")
                break
            else:
                if not is_valid_direction(position, direction):
                    print(
                        f"Found invalid direction going {starting_direction}!")
                    break
                direction = get_new_direction(position, direction)



matching_segments = {
    "L": "J",
    "J": "L",
    "F": "7",
    "7": "F"
}

loop = get_loop()
contained_tiles = []
for y, line in enumerate(lines):
    inside_loop = False
    loop_segment = None
    for x, tile in enumerate(line):
        pos = (x, y)
        if pos in loop:
            if tile == "|":
                inside_loop = not inside_loop
            elif tile in ("L", "J", "F", "7"):
                if loop_segment is None:
                    loop_segment = tile
                else:
                    if loop_segment != matching_segments[tile]:
                        inside_loop = not inside_loop
                    loop_segment = None
        elif inside_loop:
            contained_tiles.append(pos)

for y, line in enumerate(lines):
    for x, tile in enumerate(line):
        pos = (x, y)
        if pos not in loop and tile != "\n":
            if pos in contained_tiles:
                set_tile(pos, "▒")
            else:
                set_tile(pos, " ")
        else:
            set_tile(pos, tile.replace("-", "━")
                              .replace("|", "┃")
                              .replace("7", "┓")
                              .replace("F", "┏")
                              .replace("L", "┗")
                              .replace("J", "┛"))

open(sys.argv[2] if len(sys.argv) > 2 else "./loop.txt", "w").writelines(lines)