class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        def backtrack(nums, curr_per):
            if not nums:
                result.append(curr_per)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], [nums[i]] + curr_per)
       
        backtrack(nums, [])
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
    print(s.permute([0,1]))
    print(s.permute([1]))