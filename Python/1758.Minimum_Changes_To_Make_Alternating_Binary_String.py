class Solution:
    def minOperations(self, s: str) -> int:
        # get the length of the input string
        n = len(s)
        # initialize counts for two possible configurations of the string
        count1, count2 = 0, 0
        
        # loop through each character of the string
        for i in range(n):
            # if the index is even, we expect '0' at even positions and 
            # '1' at odd positions
            if i % 2 == 0:
                # count the number of characters that need to be changed to 
                # '0' at even positions
                if s[i] == '1':
                    count1 += 1
                else:
                    # count the number of characters that need to be changed 
                    # to '1' at even positions
                    count2 += 1
            else:
                # if the index is odd, we expect '1' at even positions and '0' 
                # at odd positions
                if s[i] == '0':
                    # count the number of characters that need to be changed to
                    # '1' at odd positions
                    count1 += 1
                else:
                    # count the number of characters that need to be changed to 
                    # '0' at odd positions
                    count2 += 1
        
        # return the minimum of the two counts, as we want to minimize the 
        # number of operations
        return min(count1, count2)

if __name__ == '__main__':
    s = Solution()
    print(s.minOperations("0100"))
    print(s.minOperations("1111"))
    print(s.minOperations("10"))