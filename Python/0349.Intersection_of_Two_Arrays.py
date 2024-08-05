from typing import List

class Solution(object):
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # convert both lists to sets to find the intersection (common elements)
        # after intersection convert the result back to a list
        return list(set(nums1).intersection(set(nums2)))

if __name__ == '__main__':
    s = Solution()
    print(s.intersection([1,2,2,1], [2,2]))
    print(s.intersection([4,9,5], [9,4,9,8,4]))