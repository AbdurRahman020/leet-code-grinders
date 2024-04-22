from collections import deque
from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_list = set(wordList)
        
        if endWord not in word_list:
            return 0

        q = deque()
        q.append((beginWord, 1))
        n = len(beginWord)

        while q:
            word, step = q.popleft()
            for i in range(n):
                left, right = word[:i], word[i+1:]
                for c in ascii_lowercase:
                    new_word = left + c + right
                    if new_word == endWord:
                        return step + 1
                    if new_word in word_list:
                        q.append((new_word, step + 1))
                        word_list.remove(new_word)
        
        return 0
    
if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))