import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
grid = []
directions = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
answer = 0

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        grid.append(list(line.strip()))
    rows, cols = len(grid), len(grid[0])
    for y in range(rows):
        for x in range(cols):
            rolls_around = 0
            if grid[y][x] == '.':
                continue
            for dy, dx in directions:
                ny = y + dy
                nx = x + dx
                if (0 <= ny < rows) and (0 <= nx < cols):
                    rolls_around += grid[ny][nx] == '@'
            answer += rolls_around < 4

print(answer)