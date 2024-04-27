from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
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

if __name__ == '__main__':
    s = Solution()
    print(s.findRotateSteps("godding", "gd"))
    print(s.findRotateSteps("godding", "godding"))