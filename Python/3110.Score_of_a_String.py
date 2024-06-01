class Solution:
    def scoreOfString(self, s: str) -> int:
        # initialize a variable to store the result
        result = 0
        # get the length of the string
        n = len(s)
        
        # iterate through the string, excluding the last character
        for i in range(n-1):
            # calculate the absolute difference between the ASCII values of adjacent characters
            result  += abs(ord(s[i]) - ord(s[i+1]))
        
        # return the final result
        return result 

if __name__ == '__main__':
    s = Solution()
    print(s.scoreOfString("hello"))
    print(s.scoreOfString("zaz"))