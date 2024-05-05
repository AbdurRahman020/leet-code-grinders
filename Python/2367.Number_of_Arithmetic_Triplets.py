class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        n = len(nums)
        i, j, k = 0, 1, 2
        result = 0

        while i < n and j < n and k < n:
            if nums [k] - nums[j] < diff:
                k += 1
            elif nums[j] - nums[i] < diff:
                j += 1
            elif (nums[k] - nums[j] == diff) and (nums[j] - nums[i] == diff):
                result += 1
                k += 1
            else:
                i += 1
        
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.arithmeticTriplets([0,1,4,6,7,10], 3))
    print(s.arithmeticTriplets([4,5,6,7,8,9], 2))