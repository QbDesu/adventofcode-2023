from math import prod
import sys

lines = open(sys.argv[1] if len(sys.argv)>1 else "./input.txt", "r").readlines()

gear = "*"


def check_numeric(x,y):
    if x < 0 or x >= len(lines[0]):
        return False
    if y < 0 or y >= len(lines):
        return False
    return lines[y][x].isnumeric()

def parse_no(x,y):
    cursor = x
    current_no = ""
    while check_numeric(cursor-1,y):
        cursor -= 1
    while check_numeric(cursor,y):
        current_no += lines[y][cursor]
        cursor += 1
    return int(current_no)

result = 0
adjacent_nos = []

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char is gear:
            if check_numeric(x-1,y-1):
                adjacent_nos.append(parse_no(x-1,y-1))
            if not check_numeric(x-1,y-1) and check_numeric(x,y-1):
                adjacent_nos.append(parse_no(x,y-1))
            if not check_numeric(x,y-1) and check_numeric(x+1,y-1):
                adjacent_nos.append(parse_no(x+1,y-1))
            if check_numeric(x-1,y):
                adjacent_nos.append(parse_no(x-1,y))
            if check_numeric(x+1,y):
                adjacent_nos.append(parse_no(x+1,y))
            if check_numeric(x-1,y+1):
                adjacent_nos.append(parse_no(x-1,y+1))
            if not check_numeric(x-1,y+1) and check_numeric(x,y+1):
                adjacent_nos.append(parse_no(x,y+1))
            if not check_numeric(x,y+1) and check_numeric(x+1,y+1):
                adjacent_nos.append(parse_no(x+1,y+1))
            
            if(len(adjacent_nos) == 2):
                sys.stdout.write(str(adjacent_nos) + " ")
                result += prod(adjacent_nos)
        adjacent_nos = []
    sys.stdout.write("\n")

print(f"Result: {result}")