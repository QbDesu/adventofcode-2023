from itertools import combinations
import sys

lines = open(sys.argv[1] if len(sys.argv)>1 else "./input.txt", "r").readlines()
width = len(lines[0])


galaxies = []
filled_rows = set()
filled_columns = set()

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        pos = (x, y)
        if char == "#":
            filled_rows.add(y)
            filled_columns.add(x)
            galaxies.append(pos)

def distance(pos1, pos2):
    distance = 0
    for x in range(min(pos1[0], pos2[0]), max(pos1[0], pos2[0])):
        if x in filled_columns:
            distance += 1
        else:
            distance += 1000000
    for y in range(min(pos1[1], pos2[1]), max(pos1[1], pos2[1])):
        if y in filled_rows:
            distance += 1
        else:
            distance += 1000000
    return distance


print(sum(distance(*combination) for combination in combinations(galaxies, 2)))