from collections import deque
from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # convert wordList to a set for efficient membership checking
        word_list = set(wordList)
        
        # if endWord is not in the word list, transformation is not possible
        if endWord not in word_list:
            return 0
        
        # initialize a queue to perform breadth-first search
        q = deque()
        # add the beginWord to the queue along with its transformation step
        q.append((beginWord, 1))
        # get the length of the words, assuming all words in the word list have the same length
        n = len(beginWord)
        
        # perform breadth-first search
        while q:
            # pop the word and its transformation step from the left side of the queue
            word, step = q.popleft()
            # iterate over each character position in the word
            for i in range(n):
                # split the word into left and right parts at the current character position
                left, right = word[:i], word[i+1:]
                # iterate over each lowercase letter
                for c in ascii_lowercase:
                    # generate a new word by replacing the current character with the letter
                    new_word = left + c + right
                    # if the new_word is the endWord, return the transformation step plus one
                    if new_word == endWord:
                        return step + 1
                    # if the new_word is in the word list, enqueue it with the next transformation 
                    # step and remove it from the word list to avoid revisiting it
                    if new_word in word_list:
                        q.append((new_word, step + 1))
                        word_list.remove(new_word)
        
        # if there's no transformation sequence found, return 0
        return 0
    
if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))