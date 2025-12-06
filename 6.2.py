import os
import operator
from functools import reduce

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)
answer = 0

def construct_column_ranges(op_str: str) -> list[tuple[int, int]]:
    ranges = []
    cur_start_idx = 0
    for idx, elem in enumerate(op_str[1:], 1):
        if elem in ['+', '*']:
            cur_end_idx = idx - 1
            ranges.append((cur_start_idx, cur_end_idx))
            cur_start_idx = idx
    ranges.append((cur_start_idx, len(op_str)))
    return ranges

with open(file_path, "r", encoding="utf-8") as file:
    all_lines = []
    for line in file:
        if '+' in line or '*' in line:
            operations = line
            break
        all_lines.append(line)
    all_ranges = construct_column_ranges(operations)
    func_operations = operations.strip().split()

    for column_idx, op in enumerate(func_operations):
        result_of_operations = 0 if op == '+' else 1
        func = operator.mul if op == '*' else operator.add
        levels = []

        # We can use string splitting in advance, but this does not speed up our solution, but clearly requires MUCH more memory
        # I checked with benchmark
        # like this:
        # sliced_lines = [[line[l:r] for (l, r) in all_ranges] for line in all_lines]

        for l in all_lines:
            levels.append(l[all_ranges[column_idx][0]:all_ranges[column_idx][1]])

        cur_max_len = all_ranges[column_idx][1] - all_ranges[column_idx][0]
        operands = [[] for _ in range(cur_max_len)]

        for operand_idx, cur_level in enumerate(levels):
            for right_to_left_idx in range(-1, -cur_max_len - 1, -1):
                if cur_level[right_to_left_idx] != ' ':
                    operands[right_to_left_idx].append(cur_level[right_to_left_idx])

        operands_iter = map(int, ["".join(elem) for elem in operands])
        result_of_operations = reduce(func, operands_iter)
        answer += result_of_operations

print(answer)

# "Optimised" (not) version
# def construct_column_ranges(op_str: str) -> list[tuple[int, int]]:
#     ranges = []
#     cur_start_idx = 0
#     for idx, elem in enumerate(op_str[1:], 1):
#         if elem in ['+', '*']:
#             cur_end_idx = idx - 1
#             ranges.append((cur_start_idx, cur_end_idx))
#             cur_start_idx = idx
#     ranges.append((cur_start_idx, len(op_str)))
#     return ranges
#
# with open(file_path, "r", encoding="utf-8") as file:
#     all_lines = []
#     for line in file:
#         if '+' in line or '*' in line:
#             operations = line
#             break
#         all_lines.append(line)
#     all_ranges = construct_column_ranges(operations)
#     func_operations = operations.strip().split()
#     sliced_lines = [[line[l:r] for (l, r) in all_ranges] for line in all_lines]
#
#     for column_idx, op in enumerate(func_operations):
#         result_of_operations = 0 if op == '+' else 1
#         func = operator.mul if op == '*' else operator.add
#         col_levels = [row[column_idx] for row in sliced_lines]
#         cur_max_len = all_ranges[column_idx][1] - all_ranges[column_idx][0]
#         operands = [[] for _ in range(cur_max_len)]
#
#         for operand_idx, cur_level in enumerate(col_levels):
#             for right_to_left_idx in range(-1, -cur_max_len - 1, -1):
#                 if cur_level[right_to_left_idx] != ' ':
#                     operands[right_to_left_idx].append(cur_level[right_to_left_idx])
#
#         operands_iter = map(int, ["".join(elem) for elem in operands])
#         result_of_operations = reduce(func, operands_iter)
#         answer += result_of_operations
#
# print(answer)


