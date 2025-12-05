import os

# greedy algorithm O(n)
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
answer = 0

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        bank = [int(digit) for digit in line.strip()]
        cur_max = bank.pop()
        bank_max_number = cur_max
        while bank:
            val = bank.pop()
            bank_max_number = max(val * 10 + cur_max, bank_max_number)
            cur_max = max(cur_max, val)
        answer += bank_max_number

print(answer)