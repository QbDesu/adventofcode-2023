import sys

lines = open(sys.argv[1] if len(sys.argv)>1 else "./input.txt", "r").readlines()

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
    
    def go(self, nodes, direction):
        return nodes[self.left if direction=="L" else self.right]

nodes = {}

for line in lines[2:]:
    name, destinations = line.split(" = ")
    left, right = destinations[1:-2].split(", ")
    node = Node(name, left, right)
    nodes[name] = node

def directions():
    while True:
        yield from lines[0].strip()


current_node = nodes["AAA"]
steps = 0

for direction in directions():
    if current_node.name == "ZZZ":
        break
    current_node = current_node.go(nodes, direction)
    steps += 1

print(steps)
