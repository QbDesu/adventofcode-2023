lines = open("./input.txt", "r").readlines()

result = 0

for line in lines:
    (winning_numbers, your_numbers) = [set(numbers.strip().split()) for numbers in line.split(":")[1].split("|")]
    matches = len(winning_numbers & your_numbers)
    if (matches > 0):
        result += 2**(matches-1)

print(result)
