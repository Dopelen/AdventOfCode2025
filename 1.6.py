import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
answer = 0

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        bank = [int(digit) for digit in line.strip()]
        left_border, right_border = 0, len(bank) - 11
        final_num = ""
        for i in range(12):
            next_idx = left_border + bank[left_border:right_border].index(max(bank[left_border:right_border]))
            final_num += str(bank[next_idx])
            left_border = next_idx + 1
            right_border += 1

        answer += int(final_num)

print(answer)