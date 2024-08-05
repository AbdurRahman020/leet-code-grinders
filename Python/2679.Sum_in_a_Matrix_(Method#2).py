from typing import List
import heapq

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # initialize the result variable
        result = 0
        # the dimensions of the matrix
        row_length, col_length = len(nums), len(nums[0])
        
        # sort each row in descending order
        for r in nums:
            r.sort(reverse=True)
        
        # iterate over each column
        for c in range(col_length):
            # create a max heap for the column elements
            # negate elements for max heap
            heap =[-nums[r][c] for r in range(row_length)]
            # convert list into a heap
            heapq.heapify(heap)
            # pop the max element and subtract from result
            result -= heapq.heappop(heap)
        
        # return the final result
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.matrixSum([[7,2,1],[6,4,2],[6,5,3],[3,2,1]]))
    print(s.matrixSum([[1]]))