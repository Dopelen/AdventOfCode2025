import math
import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
answer = 0
ranges = []

with open(file_path, "r", encoding="utf-8") as file:
    while (line := file.readline().strip()) != '':
        ranges.append(list(map(int, line.split('-'))))

    ranges.sort()
    ranges.append([math.inf, math.inf])
    merged_ranges = []
    cur_range = ranges[0]
    for start, end in ranges[1:]:
        if start <= cur_range[1]:
            cur_range[1] = max(cur_range[1], end)
        else:
            answer += cur_range[1] - cur_range[0] + 1
            merged_ranges.append(cur_range)
            cur_range = [start, end]

print(answer)
