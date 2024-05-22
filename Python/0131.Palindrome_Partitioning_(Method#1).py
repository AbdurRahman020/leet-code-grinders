from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
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
                current_sub_str = s[start:end]
                # if the current substring is a palindrome, continue partitioning
                if is_palindrome(current_sub_str):
                    # add the current substring to the current partition
                    path.append(current_sub_str)
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

if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))
    print(s.partition("abbab"))
    print(s.partition("a"))