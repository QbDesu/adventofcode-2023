import sys

lines = open(sys.argv[1] if len(sys.argv)>1 else "./input.txt", "r").readlines()

time = int(lines[0].split(":")[1].strip().replace(" ", ""))
record = int(lines[1].split(":")[1].strip().replace(" ", ""))

result = 0
for i in range(1,time):
    distance = i*(time-i)
    if distance > record:
        result += 1

print(result)
