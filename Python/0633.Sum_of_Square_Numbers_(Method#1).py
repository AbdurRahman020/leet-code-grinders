from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # iterate over possible values of 'a' from 0 to sqrt(c)
        for a in range(int(sqrt(c)) + 1):
            # calculate 'b' as the square root of (c - a^2)
            b = sqrt(c - a**2)
            # check if 'b' is an integer
            if b == int(b):
                # if 'b' is an integer, return True
                return True
        
        # if no such 'a' and 'b' found, return False
        return False 

if __name__ == '__main__':
    s = Solution()
    print(s.judgeSquareSum(5))
    print(s.judgeSquareSum(3))