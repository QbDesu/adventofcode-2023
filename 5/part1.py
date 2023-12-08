lines = open("./input.txt", "r").readlines()+["\n"]

values = [int(value) for value in lines[0].split(":")[1].strip().split()]
current_map = []

def map_values(current_map, values):
    new_values = []
    for value in values:
        for map_entry in current_map:
            (destination_start, source_start, length) = map_entry
            if source_start+length > value >= source_start:
                new_values.append(destination_start + (value - source_start))
                break
        else:
            new_values.append(value)
    return new_values

print(f"values ({len(values)}): {values}\n")


for line in lines[2:]:
    if line == "\n":
        values = map_values(current_map, values)
        current_map = []
        print(f"values ({len(values)}): {values}\n")
    elif ":" in line:
        continue
    else:
        current_map.append([int(item) for item in line.strip().split()])

print(min(values))