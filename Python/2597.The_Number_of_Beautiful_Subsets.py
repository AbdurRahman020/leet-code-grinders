from typing import List
from collections import defaultdict

class Solution:
    def beautifulSubsets1(self, nums: List[int], k: int) -> int:
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
    
    def beautifulSubsets2(self, nums: List[int], k: int) -> int:
        # length of the input list
        n = len(nums)
        # sorting the input list for easier comparison
        nums.sort()
        # counter for beautiful subsets
        total = 0
        
        def backtrack(index, path):
            # accessing the 'total' variable from the enclosing function
            nonlocal total
            # if the index exceeds the length of the input list, end the recursion
            if index > n:
                return
            
            # if the path is not empty, meaning it's a non-empty subset,
            # increment the total count
            if path:
                total += 1
            
            # iterate over the elements from the current index to the end of the list
            for i in range(index, n):
                # checking if the difference between nums[i] and k is not already in the path
                if nums[i] - k not in path:
                    # recursively call the function with updated index and path
                    backtrack(i+1, path + [nums[i]])
        
        # initial call to the backtrack function with index 0 and an empty path
        backtrack(0, [])
        # return the total count of beautiful subsets
        return total

if __name__ == "__main__":
    s = Solution()
    
    print(s.beautifulSubsets1([2,4,6], 1))
    print(s.beautifulSubsets1([1], 1))
    
    print(s.beautifulSubsets2([2,4,6], 1))
    print(s.beautifulSubsets2([1], 1))
