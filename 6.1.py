import os
import operator

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
answer = 0

with open(file_path, "r", encoding="utf-8") as file:
    all_lines = []
    for line in file:
        if '+' in line or '*' in line:
            operations = line.strip().split()
            break
        all_lines.append(map(int, line.strip().split()))

    for op in operations:
        cur_val = 0 if op == '+' else 1
        func = operator.mul if op == '*' else operator.add
        for iterator in all_lines:
            cur_val = func(cur_val, next(iterator))
        answer += cur_val

print(answer)