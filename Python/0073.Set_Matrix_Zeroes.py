class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # get the dimensions of the matrix
        row_length, col_length = len(matrix), len(matrix[0])
        # initialize sets to store rows and columns containing zeroes
        zero_row, zero_col = set(), set()
        
        # iterate through the matrix to find zeroes and mark corresponding rows and columns
        for r in range(row_length):
            for c in range(col_length):
                if matrix[r][c] == 0:
                    zero_row.add(r)
                    zero_col.add(c)
        
        # iterate through the matrix again and set elements in zero rows and columns to zero
        for r in range(row_length):
            for c in range(col_length):
                if r in zero_row or c in zero_col:
                    matrix[r][c] = 0

if __name__ == '__main__':
    s = Solution()
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(matrix1)
    for r in matrix1: print(r)
    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(matrix2)
    for r in matrix2: print(r)