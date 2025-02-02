from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # result stores justified lines, line_words stores words for the current line
        result, line_words = [], []
        # total characters in the current line (excluding spaces)
        total_chars = 0
        
        for word in words:
            # check if adding the new word would exceed maxWidth
            if total_chars + len(line_words) + len(word) > maxWidth:
                # distribute extra spaces
                for i in range(maxWidth - total_chars):
                    # number of gaps between words
                    num_gaps = len(line_words) - 1
                    # if only one word in the line, pad it with spaces
                    if num_gaps == 0:
                        line_words[0] += ' '
                    # distribute spaces evenly across gaps
                    else:
                        line_words[i % num_gaps] += ' '
                
                # store justified line
                result.append(''.join(line_words))
                # reset for the next line
                line_words, total_chars = [], 0
            
            # add the word to the current line
            line_words.append(word)
            # update character count
            total_chars += len(word)
        
        # last line: left-justify and pad with spaces
        last_line = ' '.join(line_words).ljust(maxWidth)
        
        # return all justified lines, including the last one
        return result + [last_line]

if __name__ == '__main__':
    s = Solution()
    print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
    print(s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain",
                         "to","a","computer.","Art","is","everything","else","we","do"], 20))
