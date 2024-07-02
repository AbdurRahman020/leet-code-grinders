from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create a Counter object to count occurrences of each number in nums1
        count_nums1 = Counter(nums1)
        # initialize an empty list to store the intersection of nums1 and nums2
        intersection = []
        
        # iterate through each number in nums2
        for num in nums2:
            # check if the number exists in count_nums1 and its count is greater than 0
            if num in count_nums1 and count_nums1[num] > 0:
                # if so, add the number to the intersection list
                intersection.append(num)
                # decrease the count of the number in count_nums1 since it's been used
                count_nums1[num] -= 1
        
        # return the list containing the intersection of nums1 and nums2
        return intersection

if __name__ == '__main__':
    s = Solution()
    print(s.intersect([1,2,2,1], [2,2]))
    print(s.intersect([4,9,5], [9,4,9,8,4]))
    print(s.intersect([10,20,30,3,4,5,100,200,500,7], [1,2,2,3,4,5,6,7]))