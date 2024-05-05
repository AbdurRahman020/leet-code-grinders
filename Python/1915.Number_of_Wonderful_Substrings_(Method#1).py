class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        """
        Counts the number of wonderful substrings in the given word.
        
        A wonderful substring is a substring where all characters occur an even number of times, 
        except for at most one character that can occur an odd number of times.
        
        :param word: The input word.
        :type word: str
        
        :return: The count of wonderful substrings in the word.
        :rtype: int
        """
        # initialize an array to store counts of different bit masks 
        # and set bit mask '0' to 1
        mask_count = [1] + [0] * 1024
        
        # initialize answer and current bit mask
        ans, bit_mask = 0, 0
        # convert the word to a list of characters
        chars = list(word)
        # iterate through each character in the word
        for c in chars:
            # calculate the index of the character in the alphabet
            index = ord(c) - 97
            # toggle the bit at the index
            bit_mask ^= 1 << index
            # increment answer by the count of the current bit mask
            ans += mask_count[bit_mask]
            
            # iterate through all possible toggled bit masks
            for i in range(10):
                ans += mask_count[bit_mask ^ (1 << i)]
            
            # increment the count of the current bit mask
            mask_count[bit_mask] += 1

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.wonderfulSubstrings("aba"))
    print(s.wonderfulSubstrings("aabb"))
    print(s.wonderfulSubstrings("he"))