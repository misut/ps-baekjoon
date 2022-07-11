# 14502. 연구소

import sys
from array import array
from collections import deque
from itertools import combinations, product

input = sys.stdin.readline


Vec2 = tuple[int, int]
Tri = tuple[Vec2, Vec2, Vec2]


def neighbors(vec: Vec2) -> list[Vec2]:
    return [
        (vec[0] - 1, vec[1]),
        (vec[0] + 1, vec[1]),
        (vec[0], vec[1] - 1),
        (vec[0], vec[1] + 1),
    ]


class Lab:
    def __init__(self, size: Vec2) -> None:
        self._arr = array("l", [0 for _ in range(size[0] * size[1])])
        self._size = size

    def __getitem__(self, pos: Vec2) -> int:
        idx = pos[0] * self._size[1] + pos[1]
        if 0 <= pos[0] < self._size[0] and 0 <= pos[1] < self._size[1]:
            return self._arr[idx]
        return 1

    def __setitem__(self, pos: Vec2, val: int) -> None:
        idx = pos[0] * self._size[1] + pos[1]
        if 0 <= pos[0] < self._size[0] and 0 <= pos[1] < self._size[1]:
            self._arr[idx] = val

    def infest(self) -> int:
        infested: set[Vec2] = set()
        viruses: deque[Vec2] = deque()

        for col, row in product(range(self._size[0]), range(self._size[1])):
            pos = (col, row)
            if self[pos] == 2:
                infested.add(pos)
                viruses.append(pos)

        while viruses:
            virus = viruses.popleft()

            for neighbor in neighbors(virus):
                if neighbor in infested or self[neighbor] != 0:
                    continue

                infested.add(neighbor)
                viruses.append(neighbor)

        return len(infested)

    def safehouse(self) -> int:
        size = self._size[0] * self._size[1]

        for val in self._arr:
            if val == 1:
                size -= 1

        return size - self.infest()


if __name__ == "__main__":
    n, m = map(int, input().split())

    lab = Lab(size=(n, m))
    empties: list[Vec2] = []
    for col in range(n):
        for row, val in enumerate(map(int, input().split())):
            if val == 0:
                empties.append((col, row))
                continue

            lab[(col, row)] = val

    answer = 0
    for one, two, thr in combinations(empties, 3):
        lab[one], lab[two], lab[thr] = 1, 1, 1

        answer = max(answer, lab.safehouse())

        lab[one], lab[two], lab[thr] = 0, 0, 0

    print(answer)
