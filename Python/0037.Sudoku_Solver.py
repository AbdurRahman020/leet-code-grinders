from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku1(self, board: List[List[str]]) -> None:
        # function to check if placing a number at position (r, c) is valid
        def isValid(r, c, num):
            # convert r and c to integers
            r, c = int(r), int(c)
            
            # check the row, column, and subgrid for the presence of the number
            for i in range(9):
                # check column
                if board[i][c] == num:
                    return False
                # check row
                if board[r][i] == num:
                    return False
                # check subgrid
                if board[3*(r//3) + i//3][3*(c//3) + i%3] == num:
                    return False
            
            return True
        
        # recursive function to solve the sudoku puzzle
        def solve1(r, c):
            # base case: if we have reached the end of the puzzle
            if r == 9:
                return True
            
            # move to the next row
            if c == 9:
                return solve1(r+1, 0)
            
            # if the current cell is empty
            if board[r][c] == '.':
                # try placing numbers from 1 to 9
                for i in range(1, 10):
                    # if placing 'i' at (r, c) is valid
                    if isValid(r, c, str(i)):
                        # place 'i' at (r, c)
                        board[r][c] = str(i)
                        
                        # recur to solve the rest of the puzzle
                        if solve1(r, c+1):
                            # if puzzle is solved, return True
                            return True
                        # backtrack if the current placement doesn't lead to a solution
                        else:
                            board[r][c] = '.'
                
                # if no valid number can be placed at (r, c), return False
                return False
            else:
                # if the current cell is not empty, move to the next cell
                return solve1(r, c+1)
        
        # start solving the puzzle from the top-left corner
        solve1(0, 0)
    
    def solveSudoku2(self, board: List[List[str]]) -> None:
        # initialize sets to keep track of numbers in rows, columns, and blocks
        rows, cols, block = defaultdict(set), defaultdict(set), defaultdict(set)
        
        # iterate through the board and populate the sets
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    block[(r//3, c//3)].add(board[r][c])
        
        def solve2(row, col):
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
                        if solve2(row, col+1):
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
                return solve2(row, col+1)
        
        # start solving the puzzle from the top-left corner
        solve2(0, 0)

if __name__ == '__main__':
    s = Solution()
    
    b1 = [["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]
    
    s.solveSudoku1(b1)
    print(b1)
    
    b2 = [["3",".",".",".",".",".",".",".","."],
          [".",".",".","6",".",".",".",".","."],
          [".","9",".",".",".",".",".",".","8"],
          [".",".",".",".","8",".",".",".","2"],
          [".","5",".","9",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".","1",".","."],
          [".",".",".",".","3",".",".",".","6"],
          [".",".",".",".",".",".",".",".","."]]
    
    s.solveSudoku2(b2)
    print(b2)
