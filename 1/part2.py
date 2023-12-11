import re
import sys

lines = open(sys.argv[1] if len(sys.argv)>1 else "./input.txt", "r").readlines()

number_regexp = re.compile(r"(?=(\d|(?:one)|(?:two)|(?:three)|(?:four)|(?:five)|(?:six)|(?:seven)|(?:eight)|(?:nine)))")

number_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}


result = 0

for line in lines:
    matches = number_regexp.finditer(line)
    matches = [match.group(1) for match in matches]
    matches = [number_to_digit[match] for match in matches]
    result += int(number_to_digit[matches[0]]+number_to_digit[matches[-1]])

print(result)
