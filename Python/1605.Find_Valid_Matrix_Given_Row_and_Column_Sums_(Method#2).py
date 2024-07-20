from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # determine the number of rows and columns in the resulting matrix
        row_length, col_length = len(rowSum), len(colSum)
        
        # initialize a matrix filled with zeros
        matrix = [[0] * col_length for _ in range(row_length)]
        
        # iterate through each cell of the matrix to fill it based on given row and column sums
        for r in range(row_length):
            for c in range(col_length):
                # fill the current cell with the minimum of remaining rowSum[r] and colSum[c]
                matrix[r][c] = min(rowSum[r], colSum[c])
                # update the remaining rowSum[r] after assigning matrix[r][c]
                rowSum[r] -= matrix[r][c] 
                # update the remaining colSum[c] after assigning matrix[r][c]
                colSum[c] -= matrix[r][c]
        
        # return the resulting matrix
        return matrix

if __name__ == '__main__':
    s = Solution()
    print(s.restoreMatrix([3,8], [4,7]))
    print(s.restoreMatrix([5,7,10], [8,6,8]))