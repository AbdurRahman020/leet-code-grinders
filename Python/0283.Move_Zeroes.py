class Solution(object):
    def moveZeroes(self, nums: list[int]) -> list:
        j, n = 0, len(nums)
        
        for i in range(n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                
        return nums
                
if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([0,1,0,3,12]))
    print(s.moveZeroes([0]))