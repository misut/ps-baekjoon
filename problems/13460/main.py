# 13460. 구슬 탈출 2

import enum
from queue import SimpleQueue

Position = tuple[int, int]


class Dir(tuple[int, int], enum.Enum):
    L = (0, -1)
    R = (0, 1)
    U = (-1, 0)
    D = (1, 0)


class Entity(str, enum.Enum):
    HOLE = "O"
    PATH = "."
    WALL = "#"


class Board:
    def __init__(self, board: dict[Position, Entity], size: tuple[int, int]) -> None:
        self._board = board
        self.size = size

    def __getitem__(self, pos: Position) -> Entity:
        return self._board.get(pos, Entity.WALL)


def move(board: Board, pos: Position, dir: Dir) -> tuple[Position, bool]:
    if board[pos] == Entity.HOLE:
        return (pos, False)
    nxt = (pos[0] + dir.value[0], pos[1] + dir.value[1])
    if board[nxt] == Entity.WALL:
        return (pos, False)
    return (nxt, True)


def tilt_board(
    board: Board, dir: Dir, red: Position, blue: Position
) -> tuple[Position, Position]:
    moved = True
    while moved:
        mred, red_moved = move(board, red, dir)
        mblue, blue_moved = move(board, blue, dir)
        if mred == mblue:
            if board[mred] == board[mblue] == Entity.HOLE:
                red, blue = mred, mblue
            break

        red, blue = mred, mblue
        moved = red_moved or blue_moved
    return (red, blue)


def solve(board: Board, red: Position, blue: Position) -> int:
    q = SimpleQueue()
    q.put((red, blue))
    visited = {(red, blue)}

    times = 1
    while times <= 10:
        nxt = SimpleQueue()
        while not q.empty():
            red, blue = q.get()
            for dir in Dir:
                mred, mblue = tilt_board(board, dir, red, blue)
                if board[mblue] == Entity.HOLE:
                    continue
                if board[mred] == Entity.HOLE:
                    return times
                if (mred, mblue) in visited:
                    continue

                nxt.put((mred, mblue))
                visited.add((mred, mblue))

        q = nxt
        times += 1

    if times > 10:
        times = -1

    return times


if __name__ == "__main__":
    n, m = map(int, input().split())

    red, blue = (0, 0), (0, 0)
    board: dict[Position, Entity] = {}
    for col in range(n):
        line = input().strip()
        for row in range(m):
            match line[row]:
                case "R":
                    red = (col, row)
                    board[(col, row)] = Entity.PATH
                case "B":
                    blue = (col, row)
                    board[(col, row)] = Entity.PATH
                case char:
                    board[(col, row)] = Entity(char)

    board = Board(board, (n, m))
    print(solve(board, red, blue))
