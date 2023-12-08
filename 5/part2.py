lines = open("./input.txt", "r").readlines()+["\n"]

class Interval():
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __and__(self, other):
        return Interval(max(self.start, other.start), min(self.stop, other.stop))
    
    def __sub__(self, other):
        return (
            Interval(self.start, max(self.start, other.start)),
            Interval(min(self.stop, other.stop), self.stop)
        )

    def __bool__(self):
        return self.start < self.stop

    def __repr__(self):
        return f"[{self.start}, {self.stop})"

values = [int(value) for value in lines[0].split(":")[1].strip().split()]
values = [Interval(values[2*i], values[2*i]+values[2*i+1]) for i in range(len(values)//2)]

def map_values(mappings, to_process):
    # sort ahead of time so the "left" leftover interval is always unmapped
    mappings.sort(key=lambda x: x[1])
    new_values = []

    while to_process:
        current_range = to_process.pop(0)
        for mapping in mappings:
            (destination_start, source_start, length) = mapping
            source_range = Interval(source_start, source_start+length)
            intersection = current_range & source_range
            if intersection:
                new_values.append(
                    Interval(
                        intersection.start - source_start + destination_start,
                        intersection.stop - source_start + destination_start
                    )
                )
                (left, right) = current_range - intersection
                if (left):
                    # because the mappings are sorted, this will always be unmapped
                    new_values.append(left)
                if (right):
                    # add to the stack to be processed
                    to_process.append(right)
                # this break is important to prevent the else clause below from running
                break
        else:
            # interval could not be mapped, so it will remain unchanged
            new_values.append(current_range)
    return new_values

current_mappings = []
for line in lines[2:]:
    if line == "\n":
        print(f"mapping...")
        print(f"values\t\t({len(values)})")
        print(f"mappings\t({len(current_mappings)})")
        values = map_values(current_mappings, values)
        print(f"result\t\t({len(values)})")
        print(f"----------------------------------")
        current_mappings = []
    elif ":" in line:
        continue
    else:
        current_mappings.append([int(item) for item in line.strip().split()])

print(min(values, key=lambda x: x.start).start)