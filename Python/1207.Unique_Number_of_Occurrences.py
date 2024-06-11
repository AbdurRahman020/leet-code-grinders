from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # count the occurrences of each element in the input list
        count = Counter(arr)
        
        # check if the number of unique occurrences is equal to the total number 
        # of unique counts if they are equal, it means each unique count appears
        # only once, making the occurrences unique
        return len(count.values()) == len(set(count.values()))

if __name__ == '__main__':
    s = Solution()
    print(s.uniqueOccurrences([1,2,2,1,1,3]))
    print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
    print(s.uniqueOccurrences([1,2]))