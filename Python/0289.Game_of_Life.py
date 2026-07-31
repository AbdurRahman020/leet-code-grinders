import random
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Applies Conway's Game of Life rules in-place.

        Uses state encoding:
        - 1  -> currently alive
        - 0  -> currently dead
        - -1 -> was alive, will die
        - 2  -> was dead, will become alive
        """
        if not board:
            return

        rows, cols = len(board), len(board[0])

        # all 8 possible neighbor directions
        directions = [(x, y) for x in (-1, 0, 1)
                      for y in (-1, 0, 1) if x or y]

        # first pass: determine next state using encoded values
        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0

                # count live neighbors
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    if (0 <= nr < rows) and (0 <= nc < cols
                                             ) and abs(board[nr][nc]) == 1:
                        live_neighbors += 1

                # apply rules
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = -1
                else:
                    if live_neighbors == 3:
                        board[r][c] = 2

        # second pass: finalize states
        for r in range(rows):
            for c in range(cols):
                board[r][c] = 1 if board[r][c] > 0 else 0

        return board


if __name__ == '__main__':
    s = Solution()

    rows, cols = 7, 8
    board = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

    s.gameOfLife(board)

    for row in board:
        print(*row)
