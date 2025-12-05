import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
answer = 0

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    no_newlines_content = content.replace('\n', '')
    ranges = [r for r in no_newlines_content.split(',')]
    total_wrong_ID = 0
    def calculate(s, e):
        current_wrong_id = 0
        current_val_s, current_val_int, e_int = s, int(s), int(e)
        while current_val_int <= e_int:
            cur_size = len(current_val_s)
            if not cur_size % 2:
                current_wrong_id += current_val_int if current_val_s[:cur_size // 2] == current_val_s[cur_size // 2:] else 0
            current_val_int += 1
            current_val_s = str(current_val_int)
        return current_wrong_id

    for i in range(len(ranges)):
        start, end = ranges[i].split('-')
        answer += calculate(start, end)

print(answer)