class Solution:
    def isMonotonic(self, nums: list[int]) -> bool: 
        if nums == sorted(nums) or nums == sorted(nums, reverse=True):
            return True
        else:
            return False
    
if __name__ == '__main__':
    s = Solution()
    print(s.isMonotonic([1,3,2]))
    print(s.isMonotonic([6,5,4,4]))
    print(s.isMonotonic([1,2,2,3]))