from typing import List

class Solution(object):
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # initialize two pointers for nums1 and nums2, and get their lengths
        i, j, n1, n2 = 0, 0, len(nums1), len(nums2) 
        
        # loop until we reach the end of either nums1 or nums2
        while i < n1 and j < n2:
            # if the current elements at i and j are equal, it's a common element
            if nums1[i] == nums2[j]:
                return nums1[i]
            # if the element in nums1 is less than the element in nums2, move 
            # to the next element in nums1
            elif nums1[i] < nums2[j]:
                i+=1
            # if the element in nums2 is less than the element in nums1, move 
            # to the next element in nums2
            else:
                j+=1
        
        # if no common element is found, return -1
        return -1
    
if __name__ == '__main__':
    s = Solution()
    print(s.getCommon([1,2,3], [2,4]))
    print(s.getCommon([1,2,3,6], [2,3,4,5]))