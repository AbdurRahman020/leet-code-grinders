class Solution:
    def maxPower(self, s: str) -> int:
        # initialize variables to keep track of count and maximum power
        count , power = 0, 0
        
        # iterate over the string starting from the second character
        for i in range(1,len(s)):
            # check if the current character is the same as the previous one
            if s[i-1] == s[i]:
                # if it is, increment the count of consecutive characters
                count += 1
                # update the maximum power encountered so far
                power = max(count, power)
            else:
                # if the current character is different from the previous one,
                # reset the count of consecutive characters
                count = 0
        
        # add 1 to the maximum power to account for the current character
        return power + 1

if __name__ == '__main__':
    s = Solution()
    print(s.maxPower("leetcode"))
    print(s.maxPower("abbcccddddeeeeedcba"))