class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list:
        """
        Finds two numbers in a list that sum up to the target.

        :param nums: The list of integers to search for the two numbers.
        :type nums: list[int]
        :param target: The target sum.
        :type target: int
        :return: A list containing the indices of the two numbers in the input list that sum up to the target.
        :rtype: list[int]
        """
        # dictionary to memoize elements already checked along with their indices
        checked = {}
        # length of the list
        n = len(nums)
        # iterate through the list 
        for i in range(n):
            # calculate the difference between the target and the current element
            diff = target - nums[i]
            # check if the difference exists in the dictionary
            if diff in checked:
                # if the difference exists, return the indices of the two elements 
                # that sum up to the target
                return [checked[diff], i]
            else:
                # otherwise, memoize the current element with its index
                checked[nums[i]] = i

if __name__ == '__main__':
    l = Solution()
    print(l.twoSum([2,7,11,15], 9))
    print(l.twoSum([3,2,4], 6))
    print(l.twoSum([-1,-2,-3,-4,-5], -8))