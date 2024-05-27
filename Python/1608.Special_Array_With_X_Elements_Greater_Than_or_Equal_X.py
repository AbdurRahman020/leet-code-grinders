from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # initialize left and right pointers for binary search
        left, right = 1, len(nums) 
        
        # binary search loop
        while(left <= right):
            # calculate the middle index
            mid = (left + right) >> 1
            
            # count the number of elements greater than or equal to mid
            count = 0
            for num in nums:
                if(num >= mid):
                    count += 1
            
            # if mid equals the count, it's a special array, return mid
            if(mid == count):
                return mid
            
            # if count is greater than mid, move left pointer to mid + 1
            if(count > mid):
                left = mid + 1
            # if count is less than mid, move right pointer to mid - 1
            else:
                right = mid - 1
        
        # if no special array found, return -1
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.specialArray([3,5]))
    print(s.specialArray([0,0]))
    print(s.specialArray([0,4,3,0,4]))