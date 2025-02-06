from bisect import bisect
from collections import defaultdict

class Solution:
    def findRotateSteps1(self, ring: str, key: str) -> int:
        # create a dictionary to store the indices of each character in the ring
        ring_index = defaultdict(list)
        
        # populate the dictionary with indices of characters in the ring
        for i, ch in enumerate(ring):
            ring_index[ch].append(i)
        
        # memoization dictionary to store already computed results
        memo = {}
        
        # define a recursive function for dynamic programming
        def dp(key_pos, ring_pos):
            # base case: if all characters in the key are processed, return 0
            if key_pos == len(key):
                return 0
            
            # check if the current state (key_pos, ring_pos) is already computed
            if (key_pos, ring_pos) in memo:
                return memo[(key_pos, ring_pos)]
            
            # initialize the minimum steps required to reach the target
            result = float('inf')
            
            # iterate through all possible positions of the current character in the ring
            for r_p in ring_index[key[key_pos]]:
                # calculate the steps needed to rotate to the current position
                steps_to_rotate = abs(ring_pos - r_p)
                # determine the minimum steps considering both clockwise and anti-clockwise rotations
                steps = min(steps_to_rotate, len(ring) - steps_to_rotate) + 1
                # recur for the next character in the key and add current steps
                steps += dp(key_pos + 1, r_p)
                # update the minimum steps required
                result = min(result, steps)
            
            # memoize the result for current state
            memo[(key_pos, ring_pos)] = result
            return result
        
        # start the dynamic programming recursion from the beginning of the key and the ring
        return dp(0, 0)
    
    def findRotateSteps2(self, ring: str, key: str) -> int:
        # get the length of the ring
        ring_length = len(ring)
        
        # create a dictionary to store indices of each character in the ring
        ch_index = defaultdict(list)
        
        for i, char in enumerate(ring):
            ch_index[char].append(i)
        
        # initialize arrays to store previous steps and indices
        # stores the minimum steps needed to reach each character of the key
        prev_steps = [0]
        # stores the indices of the ring corresponding to the previous characters
        prev_ch_index = [0]
        
        # iterate through each character in the key
        for target_ch in key:
            # get the indices of the current character in the ring
            target_indices = ch_index[target_ch]
            # initialize an array to store the minimum steps for each index
            curr_steps = [0] * len(target_indices)
            
            # iterate through each index of the current character
            for i, target_index in enumerate(target_indices):
                # find the insertion point for the current index in the previous indices array
                insert_index = bisect(prev_ch_index, target_index)
                
                # calculate the minimum distance to reach the current index
                if insert_index == len(prev_ch_index):
                    distance = min(prev_steps[-1] + target_index - prev_ch_index[-1], prev_steps[0] + prev_ch_index[0] + ring_length - target_index)
                elif insert_index == 0:
                    distance = min(prev_steps[-1] + target_index + ring_length - prev_ch_index[-1], prev_steps[0] + prev_ch_index[0] - target_index)
                else:
                    distance = min(prev_steps[insert_index - 1] + target_index - prev_ch_index[insert_index - 1], prev_steps[insert_index] + prev_ch_index[insert_index] - target_index)
                    
                # store the minimum distance in the array
                curr_steps[i] = distance
            
            # update the previous arrays with the current values
            prev_steps = curr_steps
            prev_ch_index = target_indices
        
        # return the minimum steps needed to spell out the key
        return min(curr_steps) + len(key)

if __name__ == '__main__':
    s = Solution()
    
    print(s.findRotateSteps1("godding", "gd"))
    print(s.findRotateSteps1("godding", "godding"))
    
    print(s.findRotateSteps2("godding", "gd"))
    print(s.findRotateSteps2("godding", "godding"))