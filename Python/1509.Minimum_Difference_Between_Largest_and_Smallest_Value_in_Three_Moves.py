from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # check if the length of nums is less than 5
        if len(nums) < 5:
            # if less than 5 elements, return 0 (as no meaningful comparison can be made)
            return 0
        
        # sort the array nums in non-decreasing order
        nums.sort()
        
        # calculate the minimum difference between the smallest and largest elements
        # of the subarray containing the smallest 4 elements and the subarray containing
        # the largest 4 elements after sorting nums
        return min(y - x for x, y in zip(nums[:4], nums[-4:]))

if __name__ == '__main__':
    s = Solution()
    print(s.minDifference([1,5,0,10,14]))
    print(s.minDifference([5,3,2,4]))
    print(s.minDifference([3,100,20]))