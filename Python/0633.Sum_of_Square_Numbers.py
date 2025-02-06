from math import sqrt

class Solution:
    def judgeSquareSum1(self, c: int) -> bool:
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
    
    def judgeSquareSum2(self, c: int) -> bool:
        # compute the integer square root of c
        n = int(c ** 0.5)
        # create a list of squares of integers from 0 to n
        squares = [a**2 for a in range(n+1)]
        # initialize two pointers, i starting from 0 and j starting from n
        i, j = 0, n
        
        # two-pointer technique to find if there exist integers a and b such that a^2 + b^2 = c
        while i <= j:
            # calculate the sum of squares at indices i and j
            current_sum = squares[i] + squares[j]
            
            if current_sum == c:
                # If found, return True
                return True
            elif current_sum < c:
                # If the sum is less than c, increment i to increase the sum
                i += 1
            else:
                # If the sum is greater than c, decrement j to decrease the sum
                j -= 1
        
        # If no such pair found, return False
        return False

if __name__ == '__main__':
    s = Solution()
    
    print(s.judgeSquareSum1(5))
    print(s.judgeSquareSum1(3))
    
    print(s.judgeSquareSum2(5))
    print(s.judgeSquareSum2(3))
