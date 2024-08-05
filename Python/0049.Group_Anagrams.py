from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for key, value in enumerate(strs):
            sorted_str = ''.join(sorted(value))
            anagrams[sorted_str].append(value)
            
        return list(anagrams.values())

if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["a"]))
    print(s.groupAnagrams([""]))
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))