from collections import deque
from math import sqrt

class Solution:
    def numSquares1(self, n: int) -> int:
        # if the input number is 0, return 0
        if not n:
            return 0
        
        # initialize a queue for BFS traversal, starting with the given number and 0 steps
        queue = deque([(n, 0)])
        # initialize a set to keep track of visited numbers
        visited = {n}
        
        # bfs traversal
        while queue:
            # dequeue the current number and its corresponding step count
            curr_num, step = queue.popleft()
            
            # if the current number is a perfect square, return the step count + 1
            if int(curr_num ** 0.5) == curr_num ** 0.5:
                return step + 1
            
            # iterate through all possible squares to subtract from the current number
            for i in range(int(curr_num ** 0.5) + 1):
                # calculate the next number by subtracting the square of i from the current number
                next_num = curr_num - (i ** 2)
                # if the next number hasn't been visited yet, enqueue it along with the updated step count
                if next_num not in visited:
                    queue.append((next_num, step + 1))
                    visited.add(next_num)
    
    def numSquares2(self, n: int) -> int:
        # generate a list of perfect squares up to the square root of n
        perfect_squares = [x**2 for x in range(1, int(sqrt(n))+1)]
        
        # initialize a dp array with all values set to n (maximum possible steps)
        dp = [n for _ in range(n+1)]
        # base case: 0 steps needed to reach 0
        dp[0] = 0
        
        # iterate through all numbers from 1 to n
        for i in range(1, n+1):
            # iterate through all perfect squares smaller than or equal to i
            for square in perfect_squares:
                # if subtracting a perfect square from i results in a non-negative number
                if i - square >= 0:
                    # update the dp array by taking the minimum of its current value and 1 + dp[i - square]
                    dp[i] = min(dp[i], 1 + dp[i - square])
        
        # return the result for n
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    
    print(s.numSquares1(12))
    print(s.numSquares1(13))
    
    print(s.numSquares2(12))
    print(s.numSquares2(13))
