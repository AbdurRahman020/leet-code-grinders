class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle is an empty string, return 0 (an empty string is considered to 
        # be at the start of any string)
        if not needle:
            return 0
        
        # if haystack is an empty string and needle is not empty, return -1 (needle 
        # cannot be found in an empty string)
        if not haystack:
            return -1
        
        # initialize the starting index of the window in haystack
        left = 0
        # initialize the ending index of the window. This index is one less than the
        # length of needle
        right = len(needle)-1
        
        # iterate while the right pointer is within the bounds of haystack
        while right < len(haystack):
            # extract the substring from left to right (inclusive) and compare it with needle
            if haystack[left : right+1] == needle:
                # if the substring matches needle, return the starting index of the match
                return left
            
            # move the window one position to the right
            left += 1
            right += 1
        
        # if needle was not found in haystack, return -1
        return -1
        
if __name__ == '__main__':
    s = Solution()
    print(s.strStr('leetcode', 'leetcd'))
    print(s.strStr('sadbutsad', 'sad'))