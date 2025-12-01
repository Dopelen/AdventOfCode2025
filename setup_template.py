import os

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
first, second = [], []
answer = 0

with open(file_path, "r", encoding="utf-8") as file:
    ...