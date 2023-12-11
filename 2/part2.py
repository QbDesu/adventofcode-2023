import re
from math import prod
import sys

lines = open(sys.argv[1] if len(sys.argv)>1 else "./input.txt", "r").readlines()

colors = ["red", "green", "blue"]
color_regex = {color: re.compile(r"(\d+) "+color) for color in colors}


def match_to_int(regexp, line):
    match = regexp.search(line)
    return int(match.group(1)) if match else 0


result = 0

for line in lines:
    pulls = line.split(":")[1].split(";")
    pulls = [{color: match_to_int(color_regex[color], pull)
              for color in colors} for pull in pulls]
    result += prod(max(pull[color] for pull in pulls) for color in colors)

print(result)
