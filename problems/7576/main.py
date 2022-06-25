# 7576. 토마토


M, N = 0, 0
Position = tuple[int, int]


def connected_positions(pos: Position) -> list[Position]:
    positions = [
        (pos[0] - 1, pos[1]),
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] - 1),
        (pos[0], pos[1] + 1),
    ]

    return [pos for pos in positions if 0 <= pos[0] < N and 0 <= pos[1] < M]


def propagate(
    tomatoes: dict[Position, int],
    pos: Position,
) -> list[Position]:
    propagated = []
    connected = connected_positions(pos)
    for con in connected:
        if tomatoes[con] != 0:
            continue

        tomatoes[con] = 1
        propagated.append(con)

    return propagated


def ripen(tomatoes: dict[Position, int], target: int) -> int:
    days = 0
    ripening = [pos for pos, tomato in tomatoes.items() if tomato == 1]

    current = len(ripening)
    while current != target:
        to_be_ripening = []
        for pos in ripening:
            propagated = propagate(tomatoes, pos)
            to_be_ripening.extend(propagated)

        if len(to_be_ripening) == 0:
            return -1
        ripening = to_be_ripening
        current += len(ripening)
        days += 1

    return days


def solve(tomatoes: dict[Position, int]) -> int:
    hollow = len([tomato for tomato in tomatoes.values() if tomato == -1])
    return ripen(tomatoes, M * N - hollow)


if __name__ == "__main__":
    M, N = map(int, input().strip().split())

    tomatoes = {}
    for col in range(N):
        line = map(int, input().strip().split())
        for row, ripe in enumerate(line):
            pos = (col, row)
            tomatoes[pos] = ripe

    print(solve(tomatoes), end="")
