
import sys

lines = open(sys.argv[1] if len(sys.argv)>1 else "./input.txt", "r").readlines()

time = [int(value) for value in lines[0].split(":")[1].strip().split()]
records = [int(value) for value in lines[1].split(":")[1].strip().split()]

from math import sqrt, floor, ceil

result = 1
for time, record in zip(time, records):
    even_point_1 = (time/2+sqrt((time/2)**2-record))
    even_point_2 = (time/2-sqrt((time/2)**2-record))

    lower = min(even_point_1, even_point_2)
    upper = max(even_point_1, even_point_2)

    # we need to adjust the values if the break even point is exactly on an integer
    # otherwise we would include a time that ties the record instead of beating it
    if int(lower) == lower:
        lower += 1
    if int(upper) == upper:
        upper -= 1

    result *= floor(upper)-ceil(lower)+1


print(result)
