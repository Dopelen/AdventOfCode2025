import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
answer = 0
adj_list = {}

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        key, *value = line.split()
        adj_list[key[:-1]] = value

def traverse(visited, cur_dot):
    global answer
    if cur_dot in visited:
        return
    elif cur_dot == 'out':
        answer += 1
        return
    visited.add(cur_dot)
    for neighbor in adj_list[cur_dot]:
        traverse(visited.copy(), neighbor)

traverse(set(), 'you')

print(answer)
