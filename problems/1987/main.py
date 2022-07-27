# 1987. 알파벳

import sys

answer = 0
input = sys.stdin.readline


def solve(board: list[list[int]], size: tuple[int, int]) -> int:
    global answer
    answer = 0
    c, r = size
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [False for _ in range(26)]

    def travel(col: int, row: int, cnt: int) -> None:
        global answer
        if visited[board[col][row]]:
            answer = max(answer, cnt)
            return

        for dx, dy in dirs:
            ncol = col + dx
            nrow = row + dy
            if 0 <= ncol < c and 0 <= nrow < r:
                visited[board[col][row]] = True
                travel(ncol, nrow, cnt + 1)
                visited[board[col][row]] = False

    travel(0, 0, 0)
    return answer


if __name__ == "__main__":
    c, r = map(int, input().split())

    board = []
    for _ in range(c):
        board.append([ord(ch) - ord("A") for ch in input().strip()])

    print(solve(board, (c, r)))
