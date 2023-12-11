
import sys

lines = open(sys.argv[1] if len(sys.argv)>1 else "./input.txt", "r").readlines()

time = [int(value) for value in lines[0].split(":")[1].strip().split()]
records = [int(value) for value in lines[1].split(":")[1].strip().split()]

result = 1
for time, record in zip(time, records):
    beaten = 0
    for i in range(1,time):
        distance = i*(time-i)
        if distance > record:
            beaten += 1
    result *= beaten

print(result)
