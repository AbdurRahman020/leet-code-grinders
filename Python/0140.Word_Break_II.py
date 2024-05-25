from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        # list to store valid word break combinations
        result = []
        # list to store the current combination of words being considered
        curr_word = []
        
        # backtracking function to find all valid combinations of words
        def backtrack(start):
            # if we have reached the end of the string, add the current combination to the result
            if start == n:
                result.append(" ".join(curr_word))
                return
            
            # loop through all possible end points for the current word
            for end in range(start, n):
                # extract the current word from the string
                word = s[start : end + 1]
                # if the current word is in the word dictionary
                if word in wordDict:
                    # add it to the current combination
                    curr_word.append(word)
                    # recursively call backtrack with the next start position
                    backtrack(end + 1)
                    # remove the last word from the current combination to backtrack
                    curr_word.pop()
        
        # start backtracking from the beginning of the string
        backtrack(0)
        # return the list of valid word break combinations
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
    print(s.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
    print(s.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))