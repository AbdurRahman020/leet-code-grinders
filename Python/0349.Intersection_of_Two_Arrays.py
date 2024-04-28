class Solution(object):
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1).intersection(set(nums2)))

if __name__ == '__main__':
    s = Solution()
    print(s.intersection([1,2,2,1], [2,2]))
    print(s.intersection([4,9,5], [9,4,9,8,4]))