class Solution:
    def lengthOfLastWord1(self, s: str) -> int:
        s = s.strip()
        count = 0

        for ch in s[::-1]:
            if ch == " ":
                break

            count += 1
        
        return count
    
    def lengthOfLastWord2(self, s: str) -> int:
        return len(s.strip().split(" ")[-1]) 

if __name__ == '__main__':
    s = Solution()
    
    print(s.lengthOfLastWord1("   fly me   to   the moon  "))
    print(s.lengthOfLastWord1("Hello World"))
    print(s.lengthOfLastWord1("luffy is still joyboy"))
    
    print(s.lengthOfLastWord2("   fly me   to   the moon  "))
    print(s.lengthOfLastWord2("Hello World"))
    print(s.lengthOfLastWord2("luffy is still joyboy"))
