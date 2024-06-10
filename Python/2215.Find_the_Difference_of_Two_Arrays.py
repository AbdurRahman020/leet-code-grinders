from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # convert lists to sets to get unique elements
        unique_nums1, unique_nums2 = set(nums1), set(nums2)
        
        # find the elements in nums1 that are not in nums2
        difference_in_nums1 = list(unique_nums1 - unique_nums2)
        # find the elements in nums2 that are not in nums1
        difference_in_nums2 = list(unique_nums2 - unique_nums1)
        
        # return the differences as a list of lists
        return [difference_in_nums1, difference_in_nums2]

if __name__ == '__main__':
    s = Solution()
    print(s.findDifference([1,2,3], [2,4,6])) 
    print(s.findDifference([1,2,3,3], [1,1,2,2]))