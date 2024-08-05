from typing import List
import heapq

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # initialize the result variable
        result = 0
        # get the dimensions of the matrix
        row_length, col_length = len(nums), len(nums[0])
        
        # iterate over each row in the matrix
        for r in range(row_length):
            # Convert each row into a min heap which sorts the row in ascending order
            heapq.heapify(nums[r])
        
        # iterate over each column in the matrix
        for _ in range(col_length):
            # initialize a variable to store the maximum value of the current column
            curr_max = 0
            # iterate over each row in the matrix
            for r in range(row_length):
                # pop the smallest value from the min heap of each row
                val = heapq.heappop(nums[r])
                # update the maximum value of the current column
                curr_max = max(curr_max, val)
            
            # add the maximum value of the current column to the result
            result += curr_max
        
        # return the final result
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.matrixSum([[7,2,1],[6,4,2],[6,5,3],[3,2,1]]))
    print(s.matrixSum([[1]]))