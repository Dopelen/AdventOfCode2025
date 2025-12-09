import os
from collections import deque
from itertools import combinations, pairwise
from pathlib import Path

# --- Not mine unfortunately  --- #

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "input.txt"
file_path = os.path.join(desktop, file_name)

def rectangle_area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)


def solve_part1(data: str) -> int:
    points = [tuple(map(int, line.split(","))) for line in data.splitlines()]
    return max(rectangle_area(p1, p2) for p1, p2 in combinations(points, 2))


def draw_line(grid: list[list[int]], p1: tuple[int, int], p2: tuple[int, int]):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x1] = 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][x] = 1
    else:
        raise ValueError(f"Line must be horizontal or vertical: {p1} -> {p2}")


def find_exterior(grid: list[list[int]]) -> set[tuple[int, int]]:
    ny, nx = len(grid), len(grid[0])
    exterior = set()
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        if (x, y) in exterior or not (0 <= x < nx and 0 <= y < ny) or grid[y][x] == 1:
            continue
        exterior.add((x, y))
        queue.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
    return exterior


def build_prefix_sum(ny: int, nx: int, exterior: set[tuple[int, int]]) -> list[list[int]]:
    prefix = [[0] * (nx + 1) for _ in range(ny + 1)]
    for y in range(ny):
        for x in range(nx):
            value = 0 if (x, y) in exterior else 1
            prefix[y + 1][x + 1] = value + prefix[y][x + 1] + prefix[y + 1][x] - prefix[y][x]
    return prefix


def query_rectangle(prefix: list[list[int]], p1: tuple[int, int], p2: tuple[int, int]) -> int:
    x1, x2 = sorted([p1[0], p2[0]])
    y1, y2 = sorted([p1[1], p2[1]])
    return prefix[y2 + 1][x2 + 1] - prefix[y1][x2 + 1] - prefix[y2 + 1][x1] + prefix[y1][x1]


def solve_part2(data: str) -> int:
    points = [tuple(map(int, line.split(","))) for line in data.splitlines()]

    xs = sorted({x for x, _ in points})
    ys = sorted({y for _, y in points})
    x_to_compressed = {x: i for i, x in enumerate(xs, start=1)}
    y_to_compressed = {y: i for i, y in enumerate(ys, start=1)}
    nx, ny = len(xs) + 2, len(ys) + 2

    def compress(p: tuple[int, int]) -> tuple[int, int]:
        return x_to_compressed[p[0]], y_to_compressed[p[1]]

    grid = [[0] * nx for _ in range(ny)]
    compressed_points = [compress(p) for p in points]
    for p1, p2 in pairwise(compressed_points + [compressed_points[0]]):
        draw_line(grid, p1, p2)

    exterior = find_exterior(grid)
    prefix = build_prefix_sum(ny, nx, exterior)

    result = 0
    for p1, p2 in combinations(points, 2):
        c1, c2 = compress(p1), compress(p2)
        if query_rectangle(prefix, c1, c2) == rectangle_area(c1, c2):
            result = max(result, rectangle_area(p1, p2))

    return result


if __name__ == "__main__":
    input_data = (Path(file_path).parent / "input.txt").read_text().strip()
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")