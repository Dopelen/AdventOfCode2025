import math
import os
from itertools import combinations

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
positions = []
circuits = []

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        x,y,z = map(int, line.split(","))
        positions.append((x,y,z))

pairs = []
for (i, a), (j, b) in combinations(list(enumerate(positions)), 2):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    dz = b[2] - a[2]
    dist = math.sqrt(dx*dx + dy*dy + dz*dz)
    pairs.append((dist, i, j))

pairs.sort()

def find_circuit(node):
    for idx, c in enumerate(circuits):
        if node in c:
            return idx
    return None

last_edge = None

for dist, a, b in pairs:
    ca = find_circuit(a)
    cb = find_circuit(b)

    merged = False

    if ca is None and cb is None:
        circuits.append({a, b})
        merged = True
    elif ca is not None and cb is None:
        circuits[ca].add(b)
        merged = True
    elif ca is None and cb is not None:
        circuits[cb].add(a)
        merged = True
    elif ca != cb:
        if ca > cb:
            big, small = ca, cb
        else:
            big, small = cb, ca
        circuits[small].update(circuits[big])
        del circuits[big]
        merged = True

    if merged:
        last_edge = (a, b)
        total_connected_nodes = sum(len(c) for c in circuits)
        if total_connected_nodes == len(positions):
            break

a, b = last_edge
print(positions[a][0] * positions[b][0])
