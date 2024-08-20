from typing import List
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # create a defaultdict to store the frequency of each row as a tuple
        row_map = defaultdict(int)
        # initialize a counter to keep track of the number of matching row-column pairs
        pair_count = 0
        
        # iterate over each row in the grid
        for r in grid:
            # convert the row list to a tuple and count its occurrences in row_map
            row_map[tuple(r)] += 1
        
        # iterate over each column in the grid
        for c in zip(*grid):
            # convert the column tuple to a tuple and count how many times it appears
            # in row_map, add this count to pair_count
            pair_count += row_map[tuple(c)]
        
        # return the total number of matching row-column pairs
        return pair_count

if __name__ == '__main__':
    s = Solution()
    print(s.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
    print(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))