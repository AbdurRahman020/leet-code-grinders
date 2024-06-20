class Solution:
    def reverseVowels(self, s: str) -> str:
        # convert the input string to a list of characters
        s = list(s)
        # set of vowels
        vowels = set('aeiouAEIOU')
        # pointers to traverse the string from both ends
        i, j = 0, len(s)-1
        
        # loop until the two pointers meet
        while i < j:
            # move pointer `i` until a vowel is found or `i` surpasses `j`
            if s[i] not in vowels:
                i += 1
            # move pointer `j` until a vowel is found or `j` surpasses `i`
            elif s[j] not in vowels:
                j -= 1
            else:
                # if both `s[i]` and `s[j]` are vowels, swap them
                s[i], s[j] = s[j], s[i]
                # move `i` and `j` inward
                i += 1
                j -= 1
        
        # convert the list of characters back to a string and return
        return ''.join(s)

if __name__ == '__main__':
    s = Solution()
    print(s.reverseVowels("leetcode"))
    print(s.reverseVowels("hello"))