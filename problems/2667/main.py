# 2667. 단지번호붙이기


from itertools import product


Position = tuple[int, int]


def generate_candidates(
    pos: tuple[int, int], board: dict[Position, int], visited: set[Position]
) -> list[Position]:
    candidates = [
        (pos[0] - 1, pos[1]),
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] - 1),
        (pos[0], pos[1] + 1),
    ]

    return [
        candidate
        for candidate in candidates
        if candidate in board and candidate not in visited
    ]


def find_village(
    pos: tuple[int, int], board: dict[Position, int], visited: set[Position]
) -> list[Position]:
    n = len(board)
    candidates = [pos]

    village = []
    while len(candidates) > 0:
        pos = candidates.pop(0)
        if pos not in board or pos in visited:
            continue

        visited.add(pos)
        if board[pos] == 0:
            continue

        village.append(pos)
        candidates.extend(generate_candidates(pos, board, visited))

    return village


def solve(board: dict[Position, int]) -> list[list[Position]]:
    n = len(board)
    visited = set()

    result = []
    for col, row in product(range(n), range(n)):
        pos = (col, row)
        if pos in visited:
            continue

        village = find_village(pos, board, visited)
        if len(village) > 0:
            result.append(village)

    result.sort(key=lambda v: len(v))
    return result


if __name__ == "__main__":
    n = int(input().strip())

    board = {}
    for col in range(n):
        line = input().strip()
        for row in range(n):
            pos = (col, row)
            board[pos] = int(line[row])

    result = solve(board)
    print(len(result))
    for village in result:
        print(len(village))
