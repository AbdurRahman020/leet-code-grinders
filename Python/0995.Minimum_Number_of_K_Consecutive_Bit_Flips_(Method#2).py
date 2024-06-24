from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # initialize flip_counts the number of flips performed
        flip_count = 0
        # tracks the current flip status (0 or 1)
        current_flip_status = 0
        # length of the input list
        n = len(nums)
        
        # array to track where flips are needed
        flip_needed = [False] * n
        
        # iterate through the input list
        for i in range(n):
            # if a flip is needed at the current index, toggle current_flip_status
            if flip_needed[i]:
                current_flip_status ^= 1
            
            # check if a flip is needed at the current position
            if current_flip_status ^ nums[i] == 0:
                # perform a flip
                flip_count += 1
                # toggle current_flip_status
                current_flip_status ^= 1
                
                # check if it's possible to flip k consecutive elements starting from i
                if i + k > n:
                    # if not possible, return -1
                    return -1
                
                # mark that a flip will be needed at position i+k
                if i + k < n:
                    flip_needed[i+k] = True
        
        # return the total number of flips performed
        return flip_count

if __name__ == '__main__':
    s = Solution()
    print(s.minKBitFlips([0,1,0], 1))
    print(s.minKBitFlips([1,1,0], 2))
    print(s.minKBitFlips([0,0,0,1,0,1,1,0], 3))