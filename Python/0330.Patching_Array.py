from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # initialize to track the smallest number that cannot be formed yet
        patch_needed = 0  
        # initialize to count of patches added
        patch_count = 0     
        # initialize index for iterating through nums list
        i = 0
        
        # continue until patches_needed reaches or exceeds n
        while patch_needed < n:
           # if nums[i] is within the reachable range (patch_needed + 1),
           # add nums[i] to patches_needed and move to the next number in nums
            if i < len(nums) and patch_needed + 1 >= nums[i]:
                patch_needed += nums[i]
                i += 1
            else:
                # if nums[i] is too large or beyond the range, add (patches_needed + 1)
                # to patches_needed and count this addition as a patch
                patch_needed += (patch_needed + 1)
                patch_count += 1
        
        # return the total number of patches added
        return patch_count

if __name__ == '__main__':
    s = Solution()
    print(s.minPatches([1,3], 6))
    print(s.minPatches([1,5,10], 20))
    print(s.minPatches([1,2,2], 5))