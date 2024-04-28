class Solution:
    def firstUniqChar(self, s: str) -> int:
        return min([s.index(ch) for ch in set(s) if s.count(ch) == 1] or [-1])

if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("aabb"))
    print(s.firstUniqChar("loveleetcode"))
    print(s.firstUniqChar("leetcode"))