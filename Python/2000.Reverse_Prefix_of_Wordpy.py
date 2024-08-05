class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # initialize two pointers, i and j, to 0
        i, j = 0, 0
        
        # iterate through the characters of the word
        for index, char in enumerate(word):
            # if the current character matches the target character 'ch'
            if char == ch:
                # set the end index 'j' to the index of the target character
                j = index
                # break the loop since we found the target character
                break
        
        # if 'j' is still 0, meaning 'ch' is not found, return the original word
        if j == 0:
            return word
        
        # convert the word to a list for easy character manipulation
        result = list(word)
        while i < j:
            # swap characters at indices 'i' and 'j'
            result[i], result[j] = result[j], result[i]
            # move 'i' towards the end and 'j' towards the beginning
            i += 1
            j -= 1
        
        # convert the list back to a string and return
        return ''.join(result)

if __name__ == '__main__':
    s = Solution()
    print(s.reversePrefix("abcdefd", "d"))
    print(s.reversePrefix("xyxzxe", "z"))
    print(s.reversePrefix("abcd", "z"))
    print(s.reversePrefix("rzwuktxcjfpamlonbgyieqdvhs", "s"))