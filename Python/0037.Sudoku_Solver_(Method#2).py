from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # initialize sets to keep track of numbers in rows, columns, and blocks
        rows, cols, block = defaultdict(set), defaultdict(set), defaultdict(set)
        
        # iterate through the board and populate the sets
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    block[(r//3, c//3)].add(board[r][c])
        
        def solve(row, col):
            # if reached the end of the column, move to the next row
            if col == 9:
                row += 1
                col = 0
            
            # if reached the end of the board, the puzzle is solved
            if row == 9:
                return True
            
            # if the cell is empty
            if board[row][col] == '.':
                # try each number from 1 to 9
                for ch in '123456789':
                    # check if the number is not in the current row, column, or block
                    if (
                            ch not in rows[row]
                        and ch not in cols[col]
                        and ch not in block[(row//3, col//3)]
                    ):
                        # add the number to the sets and the board
                        rows[row].add(ch)
                        cols[col].add(ch)
                        block[(row//3, col//3)].add(ch)
                        board[row][col] = ch
                        
                        # recursively solve the next cell
                        if solve(row, col+1):
                            return True
                        
                        # if no solution is found, backtrack
                        rows[row].remove(ch)
                        cols[col].remove(ch)
                        block[(row//3, col//3)].remove(ch)
                        board[row][col] = '.'
                
                # if no valid number is found, backtrack
                return False
            else:
                # if the cell is already filled, move to the next cell
                return solve(row, col+1)
        
        # start solving the puzzle from the top-left corner
        solve(0, 0)
                        
if __name__ == '__main__':
    s = Solution()
    
    b = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
    
    s.solveSudoku(b)
    print(b)