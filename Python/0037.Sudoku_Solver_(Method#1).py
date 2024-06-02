from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
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
        def solve(r, c):
            # base case: if we have reached the end of the puzzle
            if r == 9:
                return True
            
            # move to the next row
            if c == 9:
                return solve(r+1, 0)
            
            # if the current cell is empty
            if board[r][c] == '.':
                # try placing numbers from 1 to 9
                for i in range(1, 10):
                    # if placing 'i' at (r, c) is valid
                    if isValid(r, c, str(i)):
                        # place 'i' at (r, c)
                        board[r][c] = str(i)
                        
                        # recur to solve the rest of the puzzle
                        if solve(r, c+1):
                            # if puzzle is solved, return True
                            return True
                        # backtrack if the current placement doesn't lead to a solution
                        else:
                            board[r][c] = '.'
                # if no valid number can be placed at (r, c), return False
                return False
            else:
                # if the current cell is not empty, move to the next cell
                return solve(r, c+1)
        
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