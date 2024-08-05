from typing import List

class Solution(object):
    def arraySign(self, nums: List[int]) -> int:
        neg_count = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            
            if nums[i] < 0:
                neg_count +=1
        
        if neg_count % 2 == 0:
            return 1
        else:
            return -1 
        
if __name__ == '__main__':
    s = Solution()
    print(s.arraySign([-1,-2,-3,-4,3,2,1]))
    print(s.arraySign([1,5,0,2,-3]))
    print(s.arraySign([-1,1,-1,1,-1]))