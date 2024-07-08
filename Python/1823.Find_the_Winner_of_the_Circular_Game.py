class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # initialize the position index to 0 (starting position)
        pos = 0
        
        # iterate from 2 up to n (inclusive)
        for i in range(2, n+1):
            # calculate the new position using the formula for Josephus problem
            pos = (pos + k) % i
        
        # return the final position (+1 to convert from 0-based to 1-based indexing)
        return pos + 1
    
if __name__ == '__main__':
    s = Solution()
    print(s.findTheWinner(5, 2))
    print(s.findTheWinner(6, 5))