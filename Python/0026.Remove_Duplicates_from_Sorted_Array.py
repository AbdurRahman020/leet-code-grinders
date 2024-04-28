class Solution(object):
    def removeDuplicates(self, nums: list[int])-> int:
        nums[:] = sorted(set(nums))
        return len(nums)
    
if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))