from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # get the dimention of matirx
        row_length, col_length = len(grid), len(grid[0])
        
        # ensure all rows start with 1 by flipping rows where the first element is 0
        for r in range(row_length):
            if grid[r][0] == 0:
                # flip the row by toggling each element
                for c in range(col_length):
                    # toggle each element (0 to 1 or 1 to 0)
                    grid[r][c] ^= 1
        
        # ensure each column has more 1s than 0s by flipping columns if necessary
        for c in range(col_length):
            # count the number of zeros in the current column
            count_zeros = sum(grid[r][c] for r in range(row_length))
            # if there are more zeros than ones, flip the column
            if count_zeros < row_length - count_zeros:
                # flip the column by toggling each element in the column
                for r in range(row_length):
                    # toggle each element (0 to 1 or 1 to 0)
                    grid[r][c] ^= 1
        
        # calculate the total score by summing up the binary representation of each row
        total_score = 0
        for r in range(row_length):
            for c in range(col_length):
                # calculate the contribution of each element to the total score,
                # multiply the element value (0 or 1) by 2 raised to the power of 
                # its position from the right
                total_score += grid[r][c] * (1 << ((col_length - 1) - c))  

        return total_score

if __name__ == '__main__':
    s = Solution()
    print(s.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
    print(s.matrixScore([[0]]))