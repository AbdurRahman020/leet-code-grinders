class Solution:
    def firstUniqChar(self, s: str) -> int:
        # list comprehension to iterate over unique characters and find their indices
        # only consider characters with count 1 (unique)
        # if there are no unique characters, return -1
        # use the `min` function to find the minimum index among unique characters, 
        # or -1 if the list is empty
        return min([s.index(ch) for ch in set(s) if s.count(ch) == 1] or [-1])

if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("aabb"))
    print(s.firstUniqChar("loveleetcode"))
    print(s.firstUniqChar("leetcode"))