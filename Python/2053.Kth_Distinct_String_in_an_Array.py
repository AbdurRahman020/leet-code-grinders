from typing import List
from collections import Counter

class Solution:
    def kthDistinct1(self, arr: List[str], k: int) -> str:
        # create a Counter object to count occurrences of each word in the list 'arr'
        for word, count in Counter(arr).items():
            # check if the current word occurs exactly once
            if count == 1:
                # decrement k to keep track of how many distinct words we've seen
                k -= 1
                
                # if k is 0, it means we've found the k-th distinct word
                if not k:
                    # return the current word as it is the k-th distinct word
                    return word
        
        # if we exhaust the list without finding the k-th distinct word, return an empty string
        return ''
    
    def kthDistinct2(self, arr: List[str], k: int) -> str:
        # initialize an empty dictionary to count occurrences of each word
        count_dict = {}
        
        # iterate over each word in the input list 'arr'
        for word in arr:
            # if the word is already in the dictionary, increment its count
            if word in count_dict:
                count_dict[word] += 1
            # if the word is not in the dictionary, add it with a count of 1
            else:
                count_dict[word] = 1
        
        # initialize a variable to keep track of the current distinct word
        distinct_word = ""
        # initialize a counter to keep track of how many distinct words we've seen
        distinct_count = 0
        
        # iterate over each word and its count in the dictionary
        for word, count in count_dict.items():
            # check if the current word is distinct (occurs exactly once)
            if count == 1:
                # update the distinct_word with the current word
                distinct_word = word
                # increment the distinct_count
                distinct_count += 1
                
            # if distinct_count matches k, return the current distinct_word
            if distinct_count == k:
                return distinct_word
            
        # if the k-th distinct word was not found, return an empty string
        return ""

if __name__ == '__main__':
    s = Solution()
    
    print(s.kthDistinct1(["d","b","c","b","c","a"], 2))
    print(s.kthDistinct1(["aaa","aa","a"], 1))
    print(s.kthDistinct1(["a","b","a"], 3))
    
    print(s.kthDistinct2(["d","b","c","b","c","a"], 2))
    print(s.kthDistinct2(["aaa","aa","a"], 1))
    print(s.kthDistinct2(["a","b","a"], 3))
