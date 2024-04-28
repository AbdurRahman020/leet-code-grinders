class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        new_str = s.strip()
        x = new_str.split(" ")
        return len(x[-1]) 

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("   fly me   to   the moon  "))
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord("luffy is still joyboy"))