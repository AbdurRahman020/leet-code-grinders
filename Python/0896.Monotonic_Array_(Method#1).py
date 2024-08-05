from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # get the length of the input list
        n = len(nums)
        
        # check if the list is monotonically increasing, this uses a generator expression 
        # to check if every element is less than or equal to the next
        increase = all(nums[i] <= nums[i + 1] for i in range(n - 1))
        
        # check if the list is monotonically decreasing, this uses a generator expression
        # to check if every element is greater than or equal to the nex
        decrease = all(nums[i] >= nums[i + 1] for i in range(n - 1))
        
        # return True if the list is either increasing or decreasing, this means that the 
        # list is monotonic
        return increase or decrease
    
if __name__ == '__main__':
    s = Solution()
    print(s.isMonotonic([1,3,2]))
    print(s.isMonotonic([6,5,4,4]))
    print(s.isMonotonic([1,2,2,3]))