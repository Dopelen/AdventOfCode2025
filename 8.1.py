import math
import operator
import os
from functools import reduce
from itertools import combinations

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
positions = []
circuits = []
EDGE_LIMIT = 1000

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        x,y,z = map(int, line.split(","))
        positions.append((x,y,z))

pairs = []
for (i, a), (j, b) in combinations(list(enumerate(positions)), 2):
    x1, y1, z1 = a
    x2, y2, z2 = b
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    dist = math.sqrt(dx*dx + dy*dy + dz*dz)
    pairs.append((dist, i, j))

pairs.sort()

def find_circuit(node):
    for idx, c in enumerate(circuits):
        if node in c:
            return idx
    return None

processed_edges = 0

for dist, a, b in pairs:
    ca = find_circuit(a)
    cb = find_circuit(b)

    if ca is None and cb is None:
        circuits.append({a, b})
    elif ca is not None and cb is None:
        circuits[ca].add(b)
    elif ca is None and cb is not None:
        circuits[cb].add(a)
    elif ca != cb:
        circuits[ca].update(circuits[cb])
        del circuits[cb]

    processed_edges += 1
    if processed_edges == EDGE_LIMIT:
        break

sizes = sorted((len(c) for c in circuits), reverse=True)
print(reduce(operator.mul, sizes[:3]))

