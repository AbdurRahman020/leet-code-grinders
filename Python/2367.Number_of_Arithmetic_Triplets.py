from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # get the length of the nums list
        n = len(nums)
        # initialize pointers i, j, k
        i, j, k = 0, 1, 2
        # initialize the result variable to store the count of arithmetic triplets
        result = 0
        
        # loop until one of the pointers reaches the end of the list
        while i < n and j < n and k < n:
            # if the difference between nums[k] and nums[j] is less than the given difference
            if nums [k] - nums[j] < diff:
                # move k pointer forward
                k += 1
            # if the difference between nums[j] and nums[i] is less than the given difference
            elif nums[j] - nums[i] < diff:
                # move j pointer forward
                j += 1
            # if both differences equal the given difference, it's an arithmetic triplet
            elif (nums[k] - nums[j] == diff) and (nums[j] - nums[i] == diff):
                # increment the result count
                result += 1
                # move k pointer forward to check for more triplets
                k += 1
            # if none of the above conditions are met, increment i to move to the next possible triplet
            else:
                i += 1
        
        # return the total count of arithmetic triplets found
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.arithmeticTriplets([0,1,4,6,7,10], 3))
    print(s.arithmeticTriplets([4,5,6,7,8,9], 2))