class Solution:
    def judgeSquareSum(self, c: int) -> bool:
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
    print(s.judgeSquareSum(5))
    print(s.judgeSquareSum(3))