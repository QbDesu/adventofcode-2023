import re
from sys import stdout

lines = open("./input.txt", "r").readlines()

symbol = re.compile(r"[^0-9.\n]")


def check_neighbours(x,y):
    for i in range(-1,2):
        for j in range(-1,2):
            if i==0 and j==0:
                continue
            if x+i < 0 or x+i >= len(lines[0]):
                continue
            if y+j < 0 or y+j >= len(lines):
                continue
            if symbol.match(lines[y+j][x+i]):
                return True
    return False

current_no = ""
include = False
result = 0

def submit():
    global current_no, include, result
    if include:
        stdout.write(current_no + " ")
        result += int(current_no)
    current_no = ""
    include = False

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char.isnumeric():
            current_no += char
            include = include or check_neighbours(x,y)
        else:
            submit()
    stdout.write("\n")

submit()

print(f"Result: {result}")