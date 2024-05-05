class Solution(object):
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # combine the two array
        num = nums1 + nums2
        n = len(num)
        # sort the combined array
        num.sort()
        
        # if the total number of elements is odd
        if n%2 != 0:
            # return the middle element
            return num[n//2]
        else:
            # first middle element
            m1 = num[(n-1)//2]
            # second middle element
            m2 = num[(n-1)//2 + 1]
            # return the average of the two middle elements as the median
            return (float(m1) + float(m2))/2

if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,3], [2]))
    print(s.findMedianSortedArrays([1,2], [3,4]))