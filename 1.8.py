import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
grid = []
directions = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
answer = 0

def check_and_remove(f_y, f_x):
    global answer
    if grid[f_y][f_x] == '.':
        return
    rolls_around = 0
    for dy, dx in directions:
        ny = y + dy
        nx = x + dx
        if (0 <= ny < rows) and (0 <= nx < cols):
            rolls_around += grid[ny][nx] == '@'

    if rolls_around < 4:
        answer += 1
        grid[f_y][f_x] = '.'
        for dy, dx in directions:
            if (0 <= f_y + dy < rows) and (0 <= f_x + dx < cols):
                check_and_remove(f_y + dy, f_x + dx)


with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        grid.append(list(line.strip()))
    rows, cols = len(grid), len(grid[0])
    for y in range(rows):
        for x in range(cols):
            check_and_remove(y, x)


print(answer)