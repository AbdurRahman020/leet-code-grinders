from typing import List

class Solution:
    # Boyer–Moore Majority Vote Algorithm: The majority element is the one 
    # that appears more than ⌊n / 2⌋ times
    def majorityElement(self, nums: List[int]) -> int:
        count, req_num = 0, 0
        
        for n in nums:
            if count == 0:
                req_num = n
            
            if n == req_num:
                count += 1
            else:
                count -= 1
        
        return req_num

if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([3,2,3]))
    print(s.majorityElement([2,2,1,1,1,2,2]))
