from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # initialize number of words
        n = len(words)
        # initalize maximum scores for each word
        max_scores = [0 for _ in range(n)]
        # initialize scores of each word
        word_score = max_scores[:]
        # initialize frequency for each letter
        letter_freq = [0 for _ in range(26)]
        
        # calculate frequency of each letter in available letters
        for ch in letters:
            letter_freq[ord(ch) - ord('a')] += 1
        
        # calculate the score of each word based on available letters
        for i in range(n):
            word = words[i]
            for ch in word:
                code = ord(ch) - ord('a')
                if letter_freq[code] > 0:
                    word_score[i] += score[code]
                else:
                    # if letter required for the word is not available, mark score as -1
                    word_score[i] -= 1
                    break
        
        # set to store visited state during backtracking
        visited_state = set()
        
        # backtracking function to explore all possible combinations of words
        def backtrack(word_idx, curr_score, perm_key, curr_letter_freq):
            # mark the current word as visited
            perm_key |= (1 << word_idx)
            
            # base case: if all words have been considered
            if word_idx == n:
                return
            # base case: if current combination has been visited
            if perm_key in visited_state:
                return
            # base case: if current word cannot be used
            if word_score[word_idx] == -1:
                return
            # base case: check if current letter's frequency exceeds the available letters
            for i in range(26):
                if curr_letter_freq[i] > letter_freq[i]:
                    return
            
            # mark the current combination as visited
            visited_state.add(perm_key)
            # update current score
            curr_score += word_score[word_idx]
            # update max score
            max_scores[word_idx] = max(max_scores[word_idx], curr_score)
            
            # recursively explore next words
            for i in range(word_idx+1, n):
                for ch in words[i]:
                    code = ord(ch) - ord('a')
                    curr_letter_freq[code] += 1
                
                # recursive call for next word
                backtrack(i, curr_score, perm_key, curr_letter_freq)
                
                # undo changes to current letter's frequency after exploring a word
                for ch in words[i]:
                    code = ord(ch) - ord('a')
                    curr_letter_freq[code] -= 1
        
        # initialize the result
        result = 0
        
        # iterate through each word and explore possible combinations
        for i in range(n):
            # initialize current letters' frequency
            curr_letter_freq = [0 for _ in range(26)]
            for ch in words[i]:
                code = ord(ch) - ord('a')
                curr_letter_freq[code] += 1
            
            # key to mark the current word
            perm_key = 1 << i
            # start backtracking
            backtrack(i, 0, perm_key, curr_letter_freq)
            # update result with maximum score for current word
            result = max(result, max_scores[i])
        
        return result

if __name__ == '__main__':
    s = Solution()
    w1 = ["dog","cat","dad","good"]
    l1 = ["a","a","c","d","d","d","g","o","o"]
    s1 = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    print(s.maxScoreWords(w1, l1, s1))
    w2 = ["xxxz","ax","bx","cx"]
    l2 = ["z","a","b","c","x","x","x"]
    s2 = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
    print(s.maxScoreWords(w2, l2, s2))
    w3 = ["leetcode"]
    l3 = ["l","e","t","c","o","d"]
    s3 = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
    print(s.maxScoreWords(w3, l3, s3))