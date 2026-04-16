# 2533. 사회망 서비스(SNS)

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def solve(tree: dict[int, set[int]], n: int) -> int:
    earlies = {True: [0] * n, False: [0] * n}
    visited = [False] * n

    def search(node: int) -> None:
        earlies[True][node] = 1
        visited[node] = True
        for friend in tree[node]:
            if visited[friend]:
                continue

            search(friend)
            earlies[False][node] += earlies[True][friend]
            earlies[True][node] += min(earlies[True][friend], earlies[False][friend])

    search(0)
    return min(earlies[True][0], earlies[False][0])


if __name__ == "__main__":
    n = int(input())

    tree = {node: [] for node in range(n)}
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)

    print(solve(tree, n))
