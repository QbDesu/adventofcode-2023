import sys

lines = open(sys.argv[1] if len(sys.argv)>1 else "./input.txt", "r").readlines()

cards = [1] * len(lines)

for idx, line in enumerate(lines):
    (winning_numbers, your_numbers) = [set(numbers.strip().split()) for numbers in line.split(":")[1].split("|")]
    matches = len(winning_numbers & your_numbers)

    mult = cards[idx]
    for target in range(idx+1, idx+matches+1):
        cards[target] += mult

print(sum(cards))
