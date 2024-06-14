from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # initialize a list to store the frequency of each number
        freq = [0] * (max(nums) + 1)
        
        # count the frequency of each number in the input list
        for num in nums:
            freq[num] += 1
        
        # get the length of the frequency list
        n = len(freq)
        # initialize variables for tracking the current number and the total increments needed
        curr_num, increments_needed = -1, 0
        
        # iterate through the frequency list
        for i in range(n):
            # process each occurrence of the current number
            while freq[i]:
                # if the current number is less than or equal to the previous number processed
                if i <= curr_num:
                    # calculate the increments needed to make the current number unique
                    increments_needed += curr_num - i + 1
                    # move to the next number to make it unique
                    curr_num += 1
                # if the current number is greater than the previous number processed
                else:
                    # set it as the current number and process its occurrences
                    curr_num = i
                
                # decrease the frequency of the current number
                freq[i] -= 1
        
        # return the total increments needed to make all numbers unique
        return increments_needed

if __name__ == '__main__':
    s = Solution()
    print(s.minIncrementForUnique([1,2,2]))
    print(s.minIncrementForUnique([3,2,1,2,1,7]))