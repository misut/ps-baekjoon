# 1260. DFS와 BFS

import sys
from array import array
from collections import deque
from collections.abc import Iterator

input = sys.stdin.readline


class AdjMat:
    def __init__(self, num_nodes: int) -> None:
        self._graph = [
            array("l", [0 for _ in range(num_nodes)]) for __ in range(num_nodes)
        ]

    def __getitem__(self, idx: int or slice) -> None:
        if isinstance(idx, slice):
            raise IndexError(
                "AdjMat doesn't support slice as an index. Use integer index instead"
            )

        return self._graph[idx]

    def __len__(self) -> int:
        return len(self._graph)

    def connect(self, _from: int, _to: int) -> None:
        self._graph[_from][_to] = 1
        self._graph[_to][_from] = 1

    def neighbors(self, stt: int) -> Iterator[int]:
        for idx, vtx in enumerate(self._graph[stt]):
            if vtx == 0:
                continue

            yield idx


def print_bfs(mat: AdjMat, stt: int) -> None:
    q: deque[int] = deque([stt], len(mat))
    visited: set[int] = {stt}

    while q:
        cur = q.popleft()
        print(cur + 1, end=" ")

        for neighbor in mat.neighbors(cur):
            if neighbor in visited:
                continue

            q.append(neighbor)
            visited.add(neighbor)


def print_dfs(mat: AdjMat, stt: int, visited: set[int] = set()) -> None:
    visited.add(stt)
    print(stt + 1, end=" ")

    for neighbor in mat.neighbors(stt):
        if neighbor in visited:
            continue

        print_dfs(mat, neighbor, visited)


if __name__ == "__main__":
    n, m, v = map(int, input().split())

    mat = AdjMat(n)
    for _ in range(m):
        p, q = map(int, input().split())
        mat.connect(p - 1, q - 1)

    print_dfs(mat, v - 1)
    print()
    print_bfs(mat, v - 1)
