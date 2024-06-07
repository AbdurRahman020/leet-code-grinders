from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # split the input sentence into individual words
        words = sentence.split()
        # get the number of words in the sentence
        n = len(words)
        
        # iterate through each word in the sentence
        for i in range(n):
            # get the next word to process
            next_word = words[i]
            
            # iterate through each root word in the dictionary
            for root in dictionary:
                # check if the next word starts with the current root word
                if next_word.startswith(root):
                    # if the next word starts with the root word and is longer,
                    # update the next word to be the root word
                    if len(root) < len(next_word):
                        next_word = root
            
            # replace the original word with the modified word (root word)
            words[i] = next_word
        
        # join the modified words back into a single string and return
        return ' '.join(words)

if __name__ == '__main__':
    s = Solution()
    print(s.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
    print((s.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs")))