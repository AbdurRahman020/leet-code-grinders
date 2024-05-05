class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        n = len(nums)
        i, j = 0, 0
        result = []
        
        while i < n and j < n:
            if nums[j] != key:
                j += 1
            else:
                if abs(i-j) <= k:
                    result.append(i)
                
                if abs(i-j) > k and i > j:
                    j += 1
                else:
                    i += 1
                    
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.findKDistantIndices([3,4,9,1,3,9,5], 9, 1))
    print(s.findKDistantIndices([2,2,2,2,2], 2, 2))