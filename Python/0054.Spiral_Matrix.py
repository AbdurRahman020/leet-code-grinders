from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # get the dimention of matrix
        row_length, col_length = len(matrix), len(matrix[0])
        # initialize variables to track boundaries
        left, right, top, bottom = 0, col_length-1, 0, row_length-1
        # initialize a list to store the result
        result = []
        
        # iterate over the matrix in a spiral order until boundaries meet
        while left <= right and top <= bottom:
            # traverse from left to right along the top row
            for c in range(left, right+1):
                result.append(matrix[top][c])
            top += 1
            # traverse from top to bottom along the rightmost column
            for r in range(top, bottom+1):
                result.append(matrix[r][right])
            right -= 1
            # traverse from right to left along the bottom row
            for c in range(right, left-1, -1):
                result.append(matrix[bottom][c])
            bottom -=1
            # traverse from bottom to top along the leftmost column
            for r in range(bottom, top-1, -1):
                result.append(matrix[r][left])
            left +=1
        
        # return the result, truncated to the original matrix size
        return result[:row_length*col_length]

if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))