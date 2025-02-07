from typing import List
from functools import cache


class Solution:
    def maximumValueSum1(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # counter to track the number of elements where a is greater than b
        count = 0
        # variable to track the minimum absolute difference between a and b
        min_difference = float('inf')
        # variable to store the total sum of elements after choosing maximum values
        total_sum = 0
        
        # iterate through each element in nums
        for num in nums:
            # value of the element
            a = num
            # XOR operation with k to get the alternate value
            b = num^k
            # if a is greater than b, add a to the total sum
            if a > b:
                total_sum += a
            else:
                # if b is greater than or equal to a, add b to the total sum
                total_sum += b
                # increment count as b is chosen over a
                count += 1
            # update min_difference with the minimum absolute difference between a and b
            min_difference = min(min_difference, abs(a-b))
        
        # if the count of elements where b is chosen over a is odd, adjust the total sum
        if count % 2 == 1:
            total_sum -= min_difference
            
        # return the final total sum
        return total_sum
    
    def maximumValueSum2(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
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
    
    print(s.maximumValueSum1([1, 2, 1], 3, [[0, 1], [0, 2]]))
    print(s.maximumValueSum1([2, 3], 7, [[0, 1]]))
    print(s.maximumValueSum1([7, 7, 7, 7, 7, 7], 6, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]))

    print(s.maximumValueSum2([1, 2, 1], 3, [[0, 1], [0, 2]]))
    print(s.maximumValueSum2([2, 3], 7, [[0, 1]]))
    print(s.maximumValueSum2([7, 7, 7, 7, 7, 7], 6, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]))
