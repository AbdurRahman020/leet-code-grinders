class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # define a set of vowels for quick lookup
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # initialize the maximum count of vowels found in any substring of length k
        max_count = 0
        # initialize the current count of vowels in the current sliding window
        curr_count = 0
        
        # count vowels in the initial window of length k
        curr_count = sum(1 for i in range(k) if s[i] in vowels)
        
        # set the maximum count to the count from the initial window
        max_count = curr_count
        
        # slide the window across the string from position k to the end
        for i in range(k, len(s)):
            # if the new character entering the window is a vowel, increment the count
            if s[i] in vowels:
                curr_count += 1
            
            # if the character leaving the window is a vowel, decrement the count
            if s[i-k] in vowels:
                curr_count -= 1
            
            # update the maximum count if the current count is greater
            if curr_count > max_count:
                max_count = curr_count
        
        # return the maximum count of vowels found in any substring of length k
        return max_count  

if __name__ == '__main__':
    s = Solution()
    print(s.maxVowels("abciiidef", 3))
    print(s.maxVowels("aeiou", 2))
    print(s.maxVowels("leetcode", 3))