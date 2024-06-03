class Solution:
    def reverseWords(self, s: str) -> str:
        # split the input string s into a list of words using whitespace as the delimiter
        s = s.split()
        # initialize two pointers, i and j, pointing to the start and end of the list respectively
        i, j = 0, len(s) - 1
        
        # iterate until the two pointers meet or cross each other
        while i < j:
            # swap the words at positions i and j.
            s[i], s[j] = s[j], s[i]
            
            # move the pointers towards each other.
            i += 1
            j -= 1
        
        # join the reversed list of words back into a string with whitespace as the separator,
        # and strip any leading/trailing whitespaces.
        return ' '.join(s).strip() 

if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("the sky is blue"))
    print(s.reverseWords("  hello world  "))
    print(s.reverseWords("a good   example"))