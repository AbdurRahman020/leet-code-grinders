from typing import List
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # get the length of the input string
        n = len(s)
        # create a dictionary to store counts of DNA sequences
        dna_count = defaultdict(int)
        # list to store repeated DNA sequences
        repeated_seq = []
        
        # iterate over the input string, considering each sequence of length 10
        for i in range(n-9):
            # extract a sequence of length 10 from the input string
            curr_dna_seq = s[i:i+10]
            # increment the count of the extracted DNA sequence
            dna_count[curr_dna_seq] += 1
            # if the count of the DNA sequence becomes 2, it's repeated
            if dna_count[curr_dna_seq] == 2:
                # add the repeated sequence to the list
                repeated_seq.append(curr_dna_seq)
        
        # return the list of repeated DNA sequences
        return repeated_seq

if __name__ == '__main__':
    s = Solution()
    print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print(s.findRepeatedDnaSequences("AAAAAAAAAAAAA"))