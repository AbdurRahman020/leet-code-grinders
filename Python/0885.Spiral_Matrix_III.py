from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # initialize the path with the starting position
        path = [[rStart, cStart]]
        # define boundaries for the current spiral level
        top, bottom, left, right = rStart-1, rStart+1, cStart-1, cStart+1
        
        # continue until the path contains all cells in the matrix
        while len(path) < rows*cols:
            # move right across the top boundary
            for i in range(cStart+1, right+1):
                cStart = i
                # check if the new position is within bounds before adding it to the path
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    path.append([rStart, cStart])
            # expand the right boundary for the next level of the spiral
            right += 1
            
            # move down along the right boundary
            for i in range(rStart+1, bottom+1):
                rStart = i
                # check if the new position is within bounds before adding it to the path
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    path.append([rStart, cStart])
            # expand the bottom boundary for the next level of the spiral
            bottom += 1
            
            # move left across the bottom boundary
            for i in range(cStart-1, left-1, -1):
                cStart = i
                # check if the new position is within bounds before adding it to the path
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    path.append([rStart, cStart])
            # expand the left boundary for the next level of the spiral
            left -= 1
            
            # move up along the left boundary
            for i in range(rStart-1, top-1, -1):
                rStart = i
                # check if the new position is within bounds before adding it to the path
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    path.append([rStart, cStart])
            # expand the top boundary for the next level of the spiral
            top -= 1
        
        # return the complete list of positions traversed in spiral order
        return path

if __name__ == '__main__':
    s = Solution()
    # Test cases to check the implementation
    print(s.spiralMatrixIII(1, 4, 0, 0))
    print(s.spiralMatrixIII(5, 6, 1, 4))