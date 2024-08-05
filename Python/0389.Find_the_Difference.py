class Solution(object):
    def findTheDifference(self, s: str, t: str) -> str:
        # initialize a variable to store the difference in ASCII values
        string = 0
        
        # iterate over each character in string t
        for c in t:
            # add the ASCII value of the character to the string variable
            string += ord(c)
          
        # iterate over each character in string s
        for c in s:
            # subtract the ASCII value of the character from the string variable
            string -= ord(c)
        
        # convert the final ASCII value back to a character and return it
        return chr(string)
    
if __name__ == '__main__':
    s = Solution()
    print(s.findTheDifference('abcd', 'abcde'))
    print(s.findTheDifference('', 'y'))