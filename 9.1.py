import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
all_cords = []

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        x, y = map(int, line.strip().split(","))
        all_cords.append((x, y))

max_s = 0
size = len(all_cords)
for i in range(size):
    for j in range(i + 1, size):
        max_s = max(max_s, abs((all_cords[i][0] - all_cords[j][0] + 1) * (all_cords[i][1] - all_cords[j][1] + 1)))
print(max_s)

