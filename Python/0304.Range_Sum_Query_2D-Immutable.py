from typing import List

class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        # check if the matrix is empty
        if not matrix or not matrix[0]:
           # initialize an empty dp array
           self.dp = [[]]
           return
        
        # determine the number of rows and columns in the matrix
        row_length, col_length = len(matrix), len(matrix[0])
        # initialize a 2D list self.dp with dimensions row_length x col_length, filled with zeros
        # each inner list represents a row in the matrix
        # the outer list comprehension iterates over row_length to create each row,
        # and within each row, [0] * col_length creates a list of zeros of length col_length
        self.dp = [[0] * col_length for _ in range(row_length)]
        
        # build the dp array where dp[r][c] stores the sum of elements from (0,0) to (r,c)
        for r in range(row_length):
            for c in range(col_length):
                # calculate the sum of elements from the left side up to current column
                left = self.dp[r][c - 1] if c else 0
                # calculate the sum of elements from the top side down to current row
                up = self.dp[r - 1][c] if r else 0
                # adjust for double counting the top-left diagonal element
                diagonal = self.dp[r - 1][c - 1] if r and c else 0
                # compute the cumulative sum for dp[r][c] including the current matrix element
                self.dp[r][c] = matrix[r][c] + left + up - diagonal
    
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # calculate the sum of the submatrix using dp array
        # calculate sum of elements from the left side up to col1-1 for rows row1 to row2
        left = self.dp[row2][col1 - 1] if col1 else 0
        # calculate sum of elements from the top side down to row1-1 for columns col1 to col2
        up = self.dp[row1 - 1][col2] if row1 else 0
        # adjust for double counting the top-left diagonal element for the submatrix
        diagonal = self.dp[row1 - 1][col1 - 1] if row1 and col1 else 0
        
        # return the sum of the submatrix by subtracting unnecessary overlaps
        return self.dp[row2][col2] - left - up + diagonal

if __name__ == '__main__':
    commands = ["NumMatrix","sumRegion","sumRegion","sumRegion"]
    matrix = [[3, 0, 1, 4, 2],
              [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5],
              [4, 1, 0, 1, 7],
              [1, 0, 3, 0, 5]]
    
    obj = None
    output = []
    
    for i, command in enumerate(commands):
        if command == "NumMatrix":
            obj = NumMatrix(matrix)
            output.append(None)
        elif command == "sumRegion":
            if i == 1:
                output.append(obj.sumRegion(1, 1, 2, 2))
            elif i == 2:
                output.append(obj.sumRegion(2, 1, 4, 3))
            elif i == 3:
                output.append(obj.sumRegion(1, 2, 2, 4))
    
    print(output)