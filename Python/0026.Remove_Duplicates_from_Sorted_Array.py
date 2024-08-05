from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int])-> int:
        nums[:] = sorted(set(nums))
        return len(nums)
    
if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))