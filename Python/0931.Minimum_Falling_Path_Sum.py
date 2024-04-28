class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        # get the dimensions of the matrix
        row_length, col_length = len(matrix), len(matrix[0])
        
        # iterate over each row starting from the second row
        for r in range(1, row_length):
            # iterate over each column in the current row
            for c in range(col_length):
                # check if the current column is the first column
                if c == 0:
                    # if it is, add to the current element the minimum value of the element 
                    # above it and the element diagonally right above it    
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c+1])
                # check if the current column is the last column
                elif c == col_length - 1:
                    # if it is, add to the current element the minimum value of the element
                    # above it and the element diagonally left above it
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c-1])
                else:
                    # for any other column, add to the current element the minimum value of
                    # the element diagonally right above it, the element above it, and the 
                    # element diagonally left above it
                    matrix[r][c] += min(matrix[r-1][c+1], matrix[r-1][c], matrix[r-1][c-1])
        
        # return the minimum value from the last row, which represents the minimum falling path sum
        return min(matrix[-1])

if __name__ == '__main__':
    s = Solution()
    print(s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
    print(s.minFallingPathSum([[-19,57],[-40,-5]]))