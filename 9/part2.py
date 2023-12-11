import sys

lines = open(sys.argv[1] if len(sys.argv)>1 else "./input.txt", "r").readlines()

def derive(nos):
    return [nos[i+1]-nos[i] for i in range(len(nos)-1)]

def extrapolate(nos):
    if all(no==0 for no in nos):
        return 0
    else:
        return nos[0] - extrapolate(derive(nos))

result = 0
for line in lines:
    nos = [int(no) for no in line.strip().split()]
    result += extrapolate(nos)

print(result)