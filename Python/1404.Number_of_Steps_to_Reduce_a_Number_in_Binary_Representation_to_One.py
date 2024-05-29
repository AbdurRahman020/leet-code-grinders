class Solution:
    def numSteps(self, s: str) -> int:
        # convert binary string to integer
        num = int(s, 2)
        # initialize steps counter
        steps = 0
        
        # continue looping until num becomes 1
        while num != 1:
            # if num is odd (last bit is 1)
            if num & 1:
                # increment num by 1 (addition operation)
                num += 1
            # if num is even (last bit is 0)
            else:
                # right shift by 1 (division by 2)
                num >>= 1
            # increment steps counter
            steps += 1
        
        # return the total number of steps required
        return steps

if __name__ == '__main__':
    s = Solution()
    print(s.numSteps("1101"))
    print(s.numSteps("10"))
    print(s.numSteps("1"))