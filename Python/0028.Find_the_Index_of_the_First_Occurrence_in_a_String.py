class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        
if __name__ == '__main__':
    s = Solution()
    print(s.strStr('leetcode', 'leetcd'))
    print(s.strStr('sadbutsad', 'sad'))