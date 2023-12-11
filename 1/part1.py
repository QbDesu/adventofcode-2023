import re
import sys

lines = open(sys.argv[1] if len(sys.argv)>1 else "./input.txt", "r").readlines()

number_regexp = re.compile(r"(\d)")

result = 0

for line in lines:
    matches = number_regexp.findall(line)
    result += int(matches[0]+matches[-1])

print(result)
