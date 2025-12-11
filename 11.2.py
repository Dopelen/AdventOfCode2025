import os
from functools import lru_cache

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
answer = 0
adj_list = {}

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        key, *value = line.split()
        adj_list[key[:-1]] = value

@lru_cache(None)
def dfs(cur, has_dac, has_fft):
    if cur == 'out':
        return int(has_dac and has_fft)

    total = 0
    for nxt in adj_list[cur]:
        total += dfs(
            nxt,
            has_dac or (cur == 'dac'),
            has_fft or (cur == 'fft')
        )
    return total


print(dfs('svr', False, False))
