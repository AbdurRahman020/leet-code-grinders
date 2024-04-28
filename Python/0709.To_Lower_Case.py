class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

if __name__ == '__main__':
    s = Solution()
    print(s.toLowerCase("Hello"))
    print(s.toLowerCase("LOVELY"))
    print(s.toLowerCase("here"))