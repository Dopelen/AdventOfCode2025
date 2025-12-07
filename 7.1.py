import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
answer = 0

with open(file_path, "r", encoding="utf-8") as file:
    beams = {file.readline().index("S")}
    split_count = 0
    for line in file:
        if "^" not in line:
            continue
        new_beams = set()
        for beam in beams:
            if line[beam] == "^":
                split_count += 1
                if beam - 1 >= 0:
                    new_beams.add(beam - 1)
                if beam + 1 < len(line):
                    new_beams.add(beam + 1)
            else:
                new_beams.add(beam)
        beams = new_beams


print(split_count)