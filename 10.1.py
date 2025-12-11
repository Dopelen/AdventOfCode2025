import os
import sys
from collections import defaultdict, deque

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
fewest_button_presses = 0
map_states = {'.' : '#', '#' : '.'}

# Refactored one

def press_button(state, button):
    return tuple(map_states[c] if i in button else c for i, c in enumerate(state))

def fewest_presses(target, buttons_list):
    start = tuple('.' * len(target))
    target = tuple(target)
    queue = deque([(start, 0)])
    visited = {start: 0}

    while queue:
        state, dist = queue.popleft()
        if state == target:
            return dist
        for b in buttons_list:
            nxt = press_button(state, b)
            if nxt not in visited:
                visited[nxt] = dist + 1
                queue.append((nxt, dist + 1))

    return float('inf')

total = 0
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.split()
        target = parts[0][1:-1]
        buttons_raw = parts[1:-1]
        buttons_list = [list(map(int, b.strip('()').split(','))) for b in buttons_raw]
        total += fewest_presses(target, buttons_list)

print(total)


# Initial version
# Sorry guys, I have too
# sys.setrecursionlimit(3000)
#
# def pres_the_but(current_state, buttn, steps):
#     new_state = [map_states[elem] if index in buttn else elem for index, elem in enumerate(current_state)]
#     new_state_tuple = tuple(new_state)
#     if new_state_tuple not in states or states[new_state_tuple] > steps:
#         states[new_state_tuple] = steps
#     else:
#         return
#     for b in buttons_list:
#         pres_the_but(new_state, b, steps + 1)
#
#
# with open(file_path, "r", encoding="utf-8") as file:
#     for line in file:
#         current_machine = []
#         groups = line.split()
#         target = list(groups[0][1:-1])
#         buttons = groups[1:-1]
#         joltage_req = list(map(int, groups[-1][1:-1].split(',')))
#         buttons_list = []
#         for item in buttons:
#             numbers = item.strip('()').split(',')
#             int_list = list(map(int, numbers))
#             buttons_list.append(int_list)
#
#         states = defaultdict(int)
#         states[tuple(['.'] * len(target))] = 0
#         for but in buttons_list:
#             pres_the_but(['.'] * len(target), but, 1)
#         fewest_button_presses += states[tuple(target)]
#
# print(fewest_button_presses)