from typing import List

class Solution(object):
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row for validity
        for row in board:
            # list to keep track of numbers seen in the current row
            num = []
            for col in row:
                # check if the cell contains a digit
                if col.isdigit():
                    # if the digit is already in the list, it's a duplicate
                    if col in num:
                        # invalid sudoku
                        return False
                    # add the digit to the list of seen numbers for this row
                    num.append(col)
        
        # check each column for validity
        for col in range(9):
            # list to keep track of numbers seen in the current column
            num = []
            for row in range(9):
                # get the value at the current cell
                n = board[row][col]
                # check if the cell contains a digit
                if n.isdigit():
                    # if the digit is already in the list, it's a duplicate
                    if n in num:
                        # invalid sudoku
                        return False
                    # add the digit to the list of seen numbers for this column
                    num.append(n)
        
        # check each 3x3 subgrid for validity
        # loop through each row of subgrids
        for row in range(0,9,3):
            # loop through each column of subgrids
            for col in range(0,9,3):
                # list to keep track of numbers seen in the current subgrid
                num = []
                # loop through each row in the current subgrid
                for r in range(row, row+3):
                    # loop through each column in the current subgrid
                    for c in range(col, col+3):
                        # get the value at the current cell
                        n = board[r][c]
                        # check if the cell contains a digit
                        if n.isdigit():
                            # if the digit is already in the list, it's a duplicate
                            if n in num:
                                # invalid sudoku
                                return False
                            # add the digit to the list of seen numbers for this subgrid
                            num.append(n)
        
        # if no duplicates are found in any row, column, or subgrid, sudoku is valid
        return True

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

    b2 = [["8","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]

    b3 = [[".",".",".",".","5",".",".","1","."],
          [".","4",".","3",".",".",".",".","."],
          [".",".",".",".",".","3",".",".","1"],
          ["8",".",".",".",".",".",".","2","."],
          [".",".","2",".","7",".",".",".","."],
          [".","1","5",".",".",".",".",".","."],
          [".",".",".",".",".","2",".",".","."],
          [".","2",".","9",".",".",".",".","."],
          [".",".","4",".",".",".",".",".","."]]

    print(s.isValidSudoku(b1))
    print(s.isValidSudoku(b2))
    print(s.isValidSudoku(b3))