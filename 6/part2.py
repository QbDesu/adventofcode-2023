from math import sqrt, floor, ceil

lines = open("./input.txt", "r").readlines()+["\n"]

time = int(lines[0].split(":")[1].strip().replace(" ", ""))
record = int(lines[1].split(":")[1].strip().replace(" ", ""))

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

print(floor(upper)-ceil(lower)+1)
