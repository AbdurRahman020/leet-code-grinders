class Solution(object):
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        num = nums1 + nums2
        n = len(num)
        num.sort()
        
        if n%2 != 0:
            return num[n//2]
        else:
            m1 = num[(n-1)//2]
            m2 = num[(n-1)//2 + 1]
            return (float(m1) + float(m2))/2

if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,3], [2]))
    print(s.findMedianSortedArrays([1,2], [3,4]))