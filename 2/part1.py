import re

lines = open("./input.txt", "r").readlines()

game_no = re.compile(r"Game (\d+): ")

colors = ["red", "green", "blue"]
maxima = {"red": 12, "green": 13, "blue": 14}
color_regex = {color: re.compile(r"(\d+) "+color) for color in colors}

def match_to_int(regexp, line):
    match = regexp.search(line)
    return int(match.group(1)) if match else 0


def is_valid(pulls):
    return not any(any(pull[color]>maxima[color] for color in colors) for pull in pulls)


result = 0

for line in lines:
    id = int(game_no.match(line).group(1))
    pulls = line.split(":")[1].split(";")
    pulls = [{color: match_to_int(color_regex[color], pull)
              for color in colors} for pull in pulls]

    if is_valid(pulls):
        result += id

print(result)
