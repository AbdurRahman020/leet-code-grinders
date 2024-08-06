from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # count the frequency of each character in the word
        freq_count = Counter(word).values()
        
        # sort the frequencies in descending order
        sorted_freq = sorted(freq_count, reverse=True)
        
        # initialize variables to track the total number of pushes and the 
        # position in the sorted frequencies
        total_pushes = char_position = 0

        # iterate over each frequency in the sorted list
        for freq in sorted_freq:
            # calculate the number of pushes required for the current frequency,
            # `char_position // 8 + 1` determines the push count for each group 
            # of up to 8 characters
            total_pushes += freq * (char_position // 8 + 1)
            
            # move to the next position
            char_position += 1
        
        # return the total number of pushes required
        return total_pushes


if __name__ == '__main__':
    s = Solution()
    print(s.minimumPushes("abcde"))
    print(s.minimumPushes("xyzxyzxyzxyz"))
    print(s.minimumPushes("aabbccddeeffgghhiiiiii"))