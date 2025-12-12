import os
from collections import defaultdict

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
figure_num = -1
figures = defaultdict(list)
figures_data = defaultdict(list)
tasks = []

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        if line == '\n':
            continue
        elif line.strip()[-1] == ':':
            figure_num += 1
            continue
        elif '#' in line or '.' in line:
            figures[figure_num].append(list(line.strip()))
        elif 'x' in line[:5]:
            sizes, requirements = line.split(':')
            y, x = sizes.split('x')
            y = int(y)
            x = int(x)
            requirements = [int(elem) for elem in requirements.strip().split()]
            tasks.append([[y, x], requirements])

for key, value in figures.items():
    space = 0
    for line in value:
        space += line.count('#')
    figures_data[key].append(space)

total_fit = 0

for task in tasks:
    s_required = task[0][0] * task[0][1]
    s_need = sum([freq * figures_data[idx][0] for idx, freq in enumerate(task[1])])
    if s_need <= s_required:
        total_fit += 1

print(total_fit)