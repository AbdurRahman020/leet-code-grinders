from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
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

if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(12))
    print(s.numSquares(13))    