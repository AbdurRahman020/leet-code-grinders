from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # initializing two dictionaries to store frequency counts
        arr_freq, target_freq = {}, {}
        
        # iterate through each number in 'arr'
        for num in arr:
            # check if the number is not yet in 'arr_freq'
            if num not in arr_freq:
                # initialize its count to 1
                arr_freq[num] = 1
            else:
                # increment the count for the existing number
                arr_freq[num] += 1
        
        # iterate through each number in 'target'
        for num in target:
            # check if the number of unique elements differs
            if num not in target_freq:
                # initialize its count to 1
                target_freq[num] = 1
            else:
                # increment the count for the existing number
                target_freq[num] += 1
        
        # check if the number of unique elements differs
        if len(target_freq) != len(arr_freq):
            # if different, return False as the arrays can't be equal
            return False
        
        # iterate through each unique number in 'arr_freq'
        for key in arr_freq:
            # compare the counts with 'target_freq'
            if arr_freq[key] != target_freq.get(key, 0):
                # if counts don't match, return False
                return False
        
        # return True if all checks pass, meaning arrays can be equal
        return True
    
    # one liner
    # return Counter(target) == Counter(arr)

if __name__ == '__main__':
    s = Solution()
    print(s.canBeEqual([1,2,3,4], [2,4,1,3]))
    print(s.canBeEqual([7], [7]))
    print(s.canBeEqual([3,7,9], [3,7,11]))