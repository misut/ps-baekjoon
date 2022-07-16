# 1012. 유기농 배추

import sys
from collections.abc import Sequence

Pos = tuple[int, int]
input = sys.stdin.readline


def connected(a: Pos, b: Pos) -> bool:
    if a[0] == b[0] and abs(a[1] - b[1]) == 1:
        return True

    if a[1] == b[1] and abs(a[0] - b[0]) == 1:
        return True

    return False


class ConnectedComponent:
    _comp: list[Pos]

    def __init__(self, comp: Sequence[Pos]) -> None:
        self._comp = [comp[0]]

        for pos in comp[1:]:
            self.add(pos)

    def __getitem__(self, idx: int) -> Pos:
        return self._comp[idx]

    def __len__(self) -> int:
        return len(self._comp)

    def _add(self, pos: Pos) -> None:
        self._comp.append(pos)

    def add(self, pos: Pos) -> bool:
        if not self.connected(pos):
            return False

        self._add(pos)
        return True

    def connected(self, pos: Pos) -> bool:
        return any(connected(con, pos) for con in self._comp)

    def _join(self, cc: "ConnectedComponent") -> bool:
        self._comp.extend(cc._comp)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        m, n, k = map(int, input().split())
        comps: list[ConnectedComponent] = []
        for _ in range(k):
            x, y = map(int, input().split())
            pos = (x, y)
            cc_idx = []
            for idx, comp in enumerate(comps):
                if comp.connected(pos):
                    cc_idx.append(idx)

            if not cc_idx:
                comps.append(ConnectedComponent([pos]))
                continue

            cc = comps[cc_idx[0]]
            for idx in reversed(cc_idx[1:]):
                cc._join(comps[idx])
                del comps[idx]

            cc.add(pos)

        print(len(comps))
