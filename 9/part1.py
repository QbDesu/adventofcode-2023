import sys

lines = open(sys.argv[1] if len(sys.argv)>1 else "./input.txt", "r").readlines()

def derive(nos):
    return [nos[i+1]-nos[i] for i in range(len(nos)-1)]

def extrapolate(nos, reverse=False):
    if all(no==0 for no in nos):
        return 0
    elif reverse:
        return nos[0] - extrapolate(derive(nos), reverse)
    else:
        return nos[-1] + extrapolate(derive(nos), reverse)

def main(reverse=False):
    result = 0
    for line in lines:
        nos = [int(no) for no in line.strip().split()]
        result += extrapolate(nos, reverse)
    print(result)

if __name__=="__main__":
    main(reverse=False)
