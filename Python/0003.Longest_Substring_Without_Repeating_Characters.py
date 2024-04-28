class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos, result = -1, 0
        count = {}
        for i, ch in enumerate(s):
            if ch in count and count[ch] > pos:
                pos = count[ch]
            count[ch] = i
            result = max(result, i - pos)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("abcabcbb"))