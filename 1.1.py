import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
answer = 0
initial_position = 50
directions = {"L": -1, "R": 1}

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        direction = directions[line[0]]
        step = int(line[1:])
        initial_position = abs((initial_position + step * direction) % 100)
        answer += 1 if initial_position == 0 else 0

print(answer)