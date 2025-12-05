import bisect
import math
import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
answer = 0
ranges, all_ids = [], []

with open(file_path, "r", encoding="utf-8") as file:
    while (line := file.readline().strip()) != '':
        ranges.append(list(map(int, line.split('-'))))
    while (line := file.readline()):
        all_ids.append(int(line.strip()))

    ranges.sort()
    ranges.append([math.inf, math.inf])
    merged_ranges = []
    cur_range = ranges[0]
    for start, end in ranges[1:]:
        if start < cur_range[1]:
            cur_range[1] = max(cur_range[1], end)
        else:
            merged_ranges.append(cur_range)
            cur_range = [start, end]

    zip_size = len(merged_ranges)
    for id in all_ids:
        position = bisect.bisect_left(merged_ranges, [id, math.inf])
        intersection_before = intersection_after = False

        if 0 < position:
            intersection_before = merged_ranges[position - 1][0] <= id <= merged_ranges[position - 1][1]
        if position < zip_size:
            intersection_after = merged_ranges[position][0] <= id <= merged_ranges[position][1]
        answer += intersection_before or intersection_after

print(answer)
