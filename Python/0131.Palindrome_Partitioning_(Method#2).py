from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # initialize a list to store partitions for each index in the string
        partitions = [[] for _ in range(len(s))]
        
        # iterate over the string backwards, starting from the end
        for start in range(len(s)-1, -1, -1):
            # iterate over all possible substrings starting from 'start' index
            for end in range(start, len(s)):
                # extract the current substring
                sub_str = s[start:end+1]
                # check if the substring is a palindrome
                if sub_str[::-1] == sub_str:
                    # find partitions for the substring's ending index + 1
                    next_partitions = partitions[end+1] if end+1 < len(s) else [()]
                    # append each possible partition for the current substring to the list of partitions
                    for next_partition in next_partitions:
                        partitions[start].append((sub_str,) + next_partition)
        
        # return the list of partitions for the entire string starting from index 0         
        return partitions[0]

if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))
    print(s.partition("abbab"))
    print(s.partition("a"))