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


def get_new_direction(pos, direction):
    tile = get_tile(pos)
    match tile:
        case "|":
            if direction in ("N", "S"):
                return direction
        case "-":
            if direction in ("E", "W"):
                return direction
        case "L":
            if direction in ("S", "W"):
                return "E" if direction == "S" else "N"
        case "J":
            if direction in ("S", "E"):
                return "W" if direction == "S" else "N"
        case "F":
            if direction in ("N", "W"):
                return "E" if direction == "N" else "S"
        case "7":
            if direction in ("N", "E"):
                return "W" if direction == "N" else "S"


invert_direction = {
    "N": "S",
    "E": "W",
    "S": "N",
    "W": "E"
}

tile_from_directions_map = {
    ("E", "N"): "L",
    ("E", "S"): "F",
    ("E", "W"): "-",
    ("N", "S"): "|",
    ("N", "W"): "J",
    ("S", "W"): "7",
}


def tile_from_directions(a, b):
    tupled = tuple(sorted((a, b)))
    return tile_from_directions_map[tupled]


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
                set_tile(position, tile_from_directions(
                    starting_direction, invert_direction[direction]))
                return loop
            if tile == ".":
                print(f"Found break going {starting_direction}!")
                break
            else:
                direction = get_new_direction(position, direction)
                if not direction:
                    print(
                        f"Found invalid direction going {starting_direction}!")
                    break


matching_segments = {
    "L": "J",
    "J": "L",
    "F": "7",
    "7": "F"
}

loop = get_loop()
contained_tiles = 0
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
            contained_tiles += 1
print(f"Contained tiles: {contained_tiles}")
