class Solution(object):
    def findTheDifference(self, s: str, t: str) -> str:
        string = 0
        
        for c in t:
            string += ord(c)
        for c in s:
            string -= ord(c)
            
        return chr(string)
    
if __name__ == '__main__':
    s = Solution()
    print(s.findTheDifference('abcd', 'abcde'))
    print(s.findTheDifference('', 'y'))