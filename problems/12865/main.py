# 12865. 평범한 배낭

import sys

input = sys.stdin.readline


# 메모리: 43964KB / 시간: 1524ms
def solution_a() -> None:
    n, k = map(int, input().split())

    max_values = {0: 0}
    for _ in range(n):
        w, v = map(int, input().split())

        changing_values = {}
        for mw, mv in max_values.items():
            if mw + w > k:
                continue

            changing_values[mw + w] = max(mv + v, max_values.get(mw + w, 0))
        max_values.update(changing_values)

    print(max(max_values.values()))


# 메모리: 33668KB / 시간: 3760ms
def solution_b() -> None:
    n, k = map(int, input().split())

    max_values = [0 for _ in range(k + 1)]
    for _ in range(n):
        w, v = map(int, input().split())

        for weight in reversed(range(w, k + 1)):
            max_values[weight] = max(v + max_values[weight - w], max_values[weight])

    print(max_values[k])


if __name__ == "__main__":
    solution_a()
