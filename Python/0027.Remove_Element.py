class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return nums
            
if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([0,1,2,2,3,0,4,2], 2))
    print(s.removeElement([3,2,2,3], 3))