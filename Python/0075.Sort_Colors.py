from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # initialize left pointer to keep track of the position of 0s, right pointer 
        # to keep track of the position of 2s,  and current pointer to iterate through
        # the array
        left, right = 0, len(nums) - 1
        current = 0
        
        # continue until the current pointer crosses the right pointer
        while current <= right:
            # if the current element is 0, swap it with the element at the left pointer
            # and move both pointers to the right
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            # if the current element is 1, simply move the current pointer to the right
            elif nums[current] == 1:
                current += 1
            # if the current element is 2, swap it with the element at the right pointer
            # and move the right pointer to the left
            else:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1

if __name__ == '__main__':
    s = Solution()
    nums1 = [2,0,2,1,1,0]
    s.sortColors(nums1)
    print(nums1)
    nums2 = [2,0,1]
    s.sortColors(nums2)
    print(nums2)