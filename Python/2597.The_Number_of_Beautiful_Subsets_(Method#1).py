from typing import List
from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # length of the input list
        n = len(nums)
        # a defaultdict to keep track of the frequency of each number in nums
        frequency_map = defaultdict(int)
        
        # define a recursive function to backtrack through the subsets
        def backtrack(index):
            # base case: if we reach the end of the list, return 0
            if index == n:
                return 0
            
            # variable to keep track of the total count of beautiful subsets
            total = 0
            # iterate through the remaining elements in the list starting from index
            for i in range(index, n):
                # check if the current number + k and current number - k are not in the frequency_map
                if frequency_map[nums[i] + k] == 0 and frequency_map[nums[i] - k] == 0:
                    # increment the frequency of the current number
                    frequency_map[nums[i]] += 1
                    # recursively call backtrack function for the next index, and add 1 to the total
                    total += backtrack(i + 1) + 1
                    # decrement the frequency of the current number (backtrack)
                    frequency_map[nums[i]] -= 1
            return total
        
        # call the backtrack function starting from index 0 and return the result
        return backtrack(0)

if __name__ == "__main__":
    s = Solution()
    print(s.beautifulSubsets([2,4,6], 1))
    print(s.beautifulSubsets([1], 1))