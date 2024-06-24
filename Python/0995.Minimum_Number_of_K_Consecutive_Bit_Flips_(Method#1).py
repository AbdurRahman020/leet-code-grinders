from typing import List
from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
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

if __name__ == '__main__':
    s = Solution()
    print(s.minKBitFlips([0,1,0], 1))
    print(s.minKBitFlips([1,1,0], 2))
    print(s.minKBitFlips([0,0,0,1,0,1,1,0], 3))