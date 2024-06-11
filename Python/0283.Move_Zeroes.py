from typing import List

class Solution(object):
    def moveZeroes(self, nums: List[int]) -> List:
        # initialize two pointers: j for the position to swap non-zero elements,
        # and n for the length of the input list nums
        j, n = 0, len(nums)
        
        # loop through the elements of nums
        for i in range(n):
            # if the current element is not zero:
            if nums[i] != 0:
                # swap the current element with the element at position j
                nums[j], nums[i] = nums[i], nums[j]
                # increment j to move to the next position for a non-zero element
                j += 1
                
        # after the loop, all non-zero elements are moved to the beginning of nums,
        # with the original order preserved, and zeros are moved to the end
        return nums
                
if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([0,1,0,3,12]))
    print(s.moveZeroes([0]))