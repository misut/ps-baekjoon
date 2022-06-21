# 7568. 덩치


def solve(bulks: list[tuple[int, int]]) -> list[int]:
    ranks = [1 for _ in bulks]
    for idx, bulk in enumerate(bulks):
        for other in bulks:
            if bulk[0] < other[0] and bulk[1] < other[1]:
                ranks[idx] += 1

    return ranks


if __name__ == "__main__":
    n = int(input().strip())

    bulks = []
    for _ in range(n):
        x, y = [int(num) for num in input().strip().split()]
        bulks.append((x, y))

    print(*solve(bulks))
