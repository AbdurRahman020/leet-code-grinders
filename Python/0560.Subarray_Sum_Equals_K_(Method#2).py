from typing import List
from collections import defaultdict
from itertools import accumulate

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # initialize a defaultdict to store the count of prefix sums
        sum_count = defaultdict(int)
        # initialize the result variable to store the number of subarrays
        result = 0
        
        # iterate through the prefix sums of the input list nums
        for prefix_sum in [0] + list(accumulate(nums)):
            # increment the result by the count of prefix sums that satisfy the condition
            result  += sum_count[prefix_sum - k]
            # increment the count of the current prefix sum
            sum_count[prefix_sum] += 1
        
        # return the final count of subarrays
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([1,1,1], 2))
    print(s.subarraySum([1,2,3], 3))