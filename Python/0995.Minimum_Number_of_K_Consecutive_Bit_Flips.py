from typing import List
from collections import deque

class Solution:
    def minKBitFlips1(self, nums: List[int], k: int) -> int:
        # initialize the count of minimum flips required
        min_flips_count = 0
        # initialize a deque to keep track of indices where flips should end
        flip_queue = deque()
        # length of the input list
        n = len(nums)
        
        # iterate through each element in the nums array
        for i in range(n):
            # remove indices from flip_queue where flips should end (i.e., indices
            # that are no longer relevant)
            if flip_queue and flip_queue[0] == i:
                flip_queue.popleft()
            
            # check if the current element needs to be flipped
            if nums[i] == len(flip_queue) % 2:
                # check if it's possible to flip k bits starting from index i
                if i + k > n:
                    # if it's not possible to flip k bits, return -1
                    return -1
                
                # increment the flip count
                min_flips_count += 1
                # add the index where the flip ends
                flip_queue.append(i + k)
        
        # return the minimum number of flips required
        return min_flips_count
    
    def minKBitFlips2(self, nums: List[int], k: int) -> int:
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
    
    print(s.minKBitFlips1([0,1,0], 1))
    print(s.minKBitFlips1([1,1,0], 2))
    print(s.minKBitFlips1([0,0,0,1,0,1,1,0], 3))
    
    print(s.minKBitFlips2([0,1,0], 1))
    print(s.minKBitFlips2([1,1,0], 2))
    print(s.minKBitFlips2([0,0,0,1,0,1,1,0], 3))
