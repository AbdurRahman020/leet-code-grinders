from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # length of the input string
        n = len(s)
        # mapping nucleotides to integers
        nucleotide_map = {'A': 0,'T': 1,'C': 2,'G': 3}
        
        # dictionary to store seen sequences and their counts
        seen_seq = {}
        # list to store repeated sequences
        repeated_seq = []
        
        # iterate through the string, considering substrings of length 10
        for i in range(n-9):
            # initialize the current DNA sequence encoding
            curr_dna_seq = 0
            # iterate through the current substring to calculate its encodin
            for j in range(i, i+10):
                # shift left by 2 bits to make space for the next nucleotide
                curr_dna_seq <<= 2
                # add the encoded value of the current nucleotide
                curr_dna_seq |= nucleotide_map[s[j]]
            
            # get the count of the current DNA sequence in seen_seq
            count = seen_seq.get(curr_dna_seq, 0)
            # if the count is 1, this sequence has been seen before
            if count == 1:
                # append the repeated sequence to the result list
                repeated_seq.append(s[i:i+10])
                # append the repeated sequence to the result list
                seen_seq[curr_dna_seq] = 2
            # if the count is 0, this is the first occurrence of this sequence
            elif count == 0:
                # mark the sequence as seen by setting its count to 1
                seen_seq[curr_dna_seq] = 1
        
        # return the list of repeated sequences
        return repeated_seq

if __name__ == '__main__':
    s = Solution()
    print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print(s.findRepeatedDnaSequences("AAAAAAAAAAAAA"))