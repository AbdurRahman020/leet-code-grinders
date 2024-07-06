class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # initialize position
        pos = 1
        # initial direction of movement
        direction = 1
        
        # loop until time runs out
        while time > 0:
            # move to the next position
            pos += direction 
            
            # check if the position reaches the ends
            if pos == 1 or pos == n:
                # reverse direction
                direction *= -1
            
            # decrease time by 1 iteration
            time -= 1
        
        # return the final position after all iterations
        return pos

if __name__ == '__main__':
    s = Solution()
    print(s.passThePillow(4, 5))
    print(s.passThePillow(3, 2))