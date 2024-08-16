from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        row_length = len(grid)
        col_length = len(grid[0])
        
        # if the grid is smaller than 3x3, it cannot contain any 3x3 magic squares
        if row_length < 3 or col_length < 3:
            return 0
        
        # initialize the count of magic squares found
        magic_squares_count = 0
        
        # list of all possible 3x3 magic squares
        magic_sq = [
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],  # magic square 1
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],  # magic square 2
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],  # magic square 3
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],  # magic square 4
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],  # magic square 5
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],  # magic square 6
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],  # magic square 7
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]]   # magic square 8
        ]
        
        # iterate over all possible starting points (top-left corners) of 3x3 subgrids
        for r_start in range(row_length - 2):
            for c_start in range(col_length - 2):
                # extract the 3x3 subgrid starting at (r_start, c_start)
                subgrid = [grid[r_start + i][c_start:c_start + 3] for i in range(3)]
                
                # check if the extracted subgrid matches any of the predefined magic squares
                if subgrid in magic_sq:
                    # increment the count of magic squares found
                    magic_squares_count += 1
        
        # return the total count of magic squares found
        return magic_squares_count

if __name__ == '__main__':
    s = Solution()
    print(s.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
    print(s.numMagicSquaresInside([[8]]))