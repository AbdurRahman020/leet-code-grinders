from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # convert deadends list to a set for faster lookup
        dead_ends_set = set(deadends)
        # initialize a queue for BFS traversal
        queue = deque()
        # start from the initial state '0000' with 0 steps
        queue.append(('0000', 0))
        # keep track of visited states to avoid revisiting
        visited = set('0000')
        
        # perform BFS traversal
        while queue:
            # get the current state and the number of steps taken
            curr_str, curr_steps = queue.popleft()
            # if the target state is reached, return the number of steps
            if curr_str == target:
                return curr_steps
            
            # skip the current state if it is in the deadends
            if curr_str in dead_ends_set:
                continue
            
            # explore all possible next states by changing one digit at a time
            for i in range(4):
                digit = int(curr_str[i])
                for j in [1, -1]:
                    new_digit = (digit + j) % 10
                    new_str = curr_str[:i] + str(new_digit) + curr_str[i+1:]
                    
                    # if the new state is not visited, add it to the queue and mark it as visited
                    if new_str not in visited:
                        visited.add(new_str)
                        queue.append((new_str, curr_steps+1))
        
        # if the target state cannot be reached, return -1
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.openLock(["0201","0101","0102","1212","2002"], "0202"))
    print(s.openLock(["8888"], "0009"))
    print(s.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))