import os
from collections import defaultdict

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)

with (open(file_path, "r", encoding="utf-8") as file):
    beams = defaultdict(int)
    beams[file.readline().index("S")] += 1
    for line in file:
        if "^" not in line:
            continue
        new_beams = defaultdict(int)
        for beam, count in beams.items():
            if line[beam] == "^":
                if beam - 1 >= 0:
                    new_beams[beam - 1] += count
                if beam + 1 < len(line):
                    new_beams[beam + 1] += count
            else:
                new_beams[beam] += count
        beams = new_beams


print(sum(beams.values()))