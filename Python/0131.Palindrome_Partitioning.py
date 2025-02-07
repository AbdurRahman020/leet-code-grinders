from typing import List

class Solution:
    def partition1(self, s: str) -> List[List[str]]:
        # define a helper function to check if a string is a palindrome
        def is_palindrome(sub_str):
            return sub_str == sub_str[::-1]
        
        # define a recursive backtracking function
        def backtrack(start, path):
            # if we've reached the end of the string, add the current partition to the result
            if start == len(s):
                # make a copy of the current partition and add it to the result
                result.append(path[:])
                return
            
            # iterate over all possible end indices for the current partition
            for end in range(start+1, len(s)+1):
                # extract the current substring
                curr_sub_str = s[start:end]
                # if the current substring is a palindrome, continue partitioning
                if is_palindrome(curr_sub_str):
                    # add the current substring to the current partition
                    path.append(curr_sub_str)
                    # recur with the next start index
                    backtrack(end, path)
                    # backtrack by removing the last added substring from the current partition
                    path.pop()
        
        # initialize an empty list to store the result
        result = []
        # start backtracking from the beginning of the string with an empty partition
        backtrack(0, [])
        # return the final result
        return result
    
    def partition2(self, s: str) -> List[List[str]]:
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
    
    print(s.partition1("aab"))
    print(s.partition1("abbab"))
    print(s.partition1("a"))
    
    print(s.partition2("aab"))
    print(s.partition2("abbab"))
    print(s.partition2("a"))