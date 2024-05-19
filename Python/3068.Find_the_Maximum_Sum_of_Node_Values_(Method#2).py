from typing import List
from functools import cache


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # get the length of the input list nums
        n = len(nums)

        # decorator to memoize/cache function results for faster computation
        @cache
        def calculateMaximumValueSum(index, count):
            # base case: if we reach the end of the list nums
            if index == n:
                # if there's only one node included in the path
                if count == 1:
                    # return a very large negative number
                    return -float("inf")
                # otherwise, return 0 as there are no more nodes to consider
                return 0
            # get the value of the current node
            value = nums[index]
            # calculate the maximum value sum by either including or excluding the current node
            return max(
                value + calculateMaximumValueSum(index + 1, count),
                (value ^ k) + calculateMaximumValueSum(index + 1, count + 1),
            )

        # start the recursion from the first index (0) with a counter of 0
        return calculateMaximumValueSum(0, 0)


if __name__ == "__main__":
    s = Solution()
    print(s.maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]]))
    print(s.maximumValueSum([2, 3], 7, [[0, 1]]))
    print(s.maximumValueSum([7, 7, 7, 7, 7, 7], 6, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]))
