from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(i, xor_total):
            # base case: when the index reaches the length of nums, return the XOR total
            if i == len(nums):
                return xor_total
            # recursive step: for each element in nums, we have two choices,
            # either include it in the subset or exclude it
            # so, recursively call backtrack with both choices and XOR the result
            return backtrack(i+1, xor_total^nums[i]) + backtrack(i+1, xor_total)
        
        # start the backtracking from the beginning (index 0) with XOR total 
        # initialized to 0
        return backtrack(0, 0)        

if __name__ == '__main__':
    s = Solution()
    print(s.subsetXORSum([1,3]))
    print(s.subsetXORSum([5,1,6]))
    print(s.subsetXORSum([3,4,5,6,7,8]))