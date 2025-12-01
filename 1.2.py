import os

# My terrible mistake was thinking I could immediately write a solution using the leftovers,
# which led me into a bottomless abyss of debugging. Pride was my undoing.

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
answer = 0
position = 50
directions = {"L": -1, "R": 1}

# Smart version
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        direction = directions[line[0]]
        value = int(line[1:])
        target = ((100 - position) if direction == 1 else position) % 100
        i_first = target if target != 0 else 100
        count = (1 + (value - i_first) // 100) if value >= i_first else 0
        answer += count
        position = (position + value * direction) % 100
print(answer)

# Initial version
answer = 0
position = 50
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        direction = line[0]
        value = int(line[1:])

        while value > 0:
            position = position + (1 if direction == "R" else -1)
            value -= 1

            if position < 0:
                position = 99
            elif position > 99:
                position = 0

            if position == 0:
                answer += 1

print(answer)