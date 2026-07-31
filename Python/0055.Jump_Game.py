from typing import List

class Solution:
    def canJump1(self, nums: List[int]) -> bool:
        # initialize the maximum remaining jumps available
        jump = 0
        
        # iterate through each jump value in the array
        for n in nums:
            # if no jumps are left before reaching the current position, return False
            if jump < 0:
                return False
            # if the current position provides more jumps, update the maximum remaining jumps
            elif n > jump:
                jump = n
            
            # use one jump to move to the next position
            jump -= 1
        
        # if all positions are successfully reached, return True
        return True
    
    def canJump2(self, nums: List[int]) -> bool:
        # store the length of the input array
        n = len(nums)
        
        # initialize a dp array to store the farthest reachable index at each position
        dp = [0] * n
        
        # initialize the farthest reachable index from the starting position
        dp[0] = nums[0]

        # iterate through each position except the last one
        for i in range(1, n - 1):
            # if the current position cannot be reached, return False
            if dp[i-1] < i:
                return False
                
            # update the farthest reachable index from the current position
            dp[i] = max(i + nums[i], dp[i - 1])
            
            # if the last index is reachable, return True
            if dp[i] >= n - 1:
                return True
        
        # return whether the last index is reachable
        return dp[n - 2] >= n - 1


if __name__ == '__main__':
    s = Solution()
    
    print(s.canJump1([2,3,1,1,4]))
    print(s.canJump1([3,2,1,0,4]))
    
    print(s.canJump2([2,3,1,1,4]))
    print(s.canJump2([3,2,1,0,4]))