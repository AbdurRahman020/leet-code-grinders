from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # get the length of list
        n = len(nums)
        # using any() function to check if there exists any triplet (i, j, k) 
        # where i < j < k and nums[i] < nums[j] < nums[k]
        # if any such triplet exists, return True; otherwise, return False
        return any(
            nums[i] < nums[j] < nums[k]
            for i in range(n)               # iterate over all possible values of i
            for j in range(i + 1, n)        # iterate over all possible values of j such that j > i
            for k in range(j + 1, n)        # iterate over all possible values of k such that k > j
            )

if __name__ == '__main__':
    s = Solution()
    print(s.increasingTriplet([1,2,3,4,5]))
    print(s.increasingTriplet([5,4,3,2,1]))
    print(s.increasingTriplet([2,1,5,0,4,6]))