import os
from functools import lru_cache

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
answer = 0

def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

divisors = {n: find_divisors(n) for n in range(1, 100)}

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    no_newlines_content = content.replace('\n', '')
    ranges = [r for r in no_newlines_content.split(',')]
    total_wrong_ID = 0

    def check_for_pattern(input):
        div = divisors[len(input)]
        for d in div[:-1]:
            chunk_size = len(input) // d
            chunk = input[:d]
            if chunk * chunk_size == input:
                return True
        return False

    def calculate(s, e):
        current_wrong_id = 0
        current_val_s, current_val_int, e_int = s, int(s), int(e)
        while current_val_int <= e_int:
            if check_for_pattern(current_val_s):
                current_wrong_id += current_val_int
            current_val_int += 1
            current_val_s = str(current_val_int)
        return current_wrong_id

    for i in range(len(ranges)):
        start, end = ranges[i].split('-')
        answer += calculate(start, end)

print(answer)