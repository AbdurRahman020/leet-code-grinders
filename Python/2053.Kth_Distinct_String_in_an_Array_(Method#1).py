from typing import List
from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
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

if __name__ == '__main__':
    s = Solution()
    print(s.kthDistinct(["d","b","c","b","c","a"], 2))
    print(s.kthDistinct(["aaa","aa","a"], 1))
    print(s.kthDistinct(["a","b","a"], 3))