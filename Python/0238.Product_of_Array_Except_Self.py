from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get the length of list 
        n = len(nums)
        
        # initialize two lists, prefix and suffix, both with length n and filled with 1
        # prefix[i] will store the product of all elements to the left of nums[i]
        # suffix[i] will store the product of all elements to the right of nums[i]
        prefix = [1] * n
        suffix = [1] * n
        
        # calculate prefix products
        for i in range(1, n):
            # multiply prefix[i-1] with nums[i-1] to get prefix[i]
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # calculate suffix products
        for i in range(n-2, -1, -1):
            # multiply suffix[i+1] with nums[i+1] to get suffix[i]
            suffix[i] = suffix[i+1] * nums[i+1]
        
        # initialize a new list arr to store the final result
        # each element in arr will be the product of prefix[i] and suffix[i]
        arr = [prefix[i] * suffix[i] for i in range(n)]
        
        # return the final arr.
        return arr

if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))
    print(s.productExceptSelf([-1,1,0,-3,3]))