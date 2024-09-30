# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
# otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # initialize the range for the guessing number
        low, high = 1, n
        
        # continue searching while the range is valid
        while low < high:
            # calculate the midpoint of the current range, using bitwise right 
            # shift for efficiency
            mid = (low + high) >> 1  
            
            # use the guess API to check if mid is the correct number
            if guess(mid) <= 0:
                # if guess returns -1 or 0, the picked number is less than or equal 
                # to mid, narrow the search to the lower half (including mid)
                high = mid 
            else:
                # if guess returns 1, the picked number is greater than mid,w
                # narrow the search to the upper half (excluding mid)
                low = mid + 1
        
        # when low meets high, it is the guessed number
        return low


if __name__ == '__main__':
    s = Solution()
    print(s.guessNumber(10))
    print(s.guessNumber(1))
    print(s.guessNumber(2))