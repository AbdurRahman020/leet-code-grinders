class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        """
        Finds the maximum integer in the input list such that its sum with another integer in the list equals 0.
        
        This method sorts the input list of integers and then iterates through it with two pointers,
        one starting from the beginning and the other starting from the end. It moves the pointers towards each other
        and returns the maximum integer found such that its sum with another integer in the list equals 0.
        
        :param nums: A list of integers.
        :type nums: list[int]
        
        :return: The maximum integer in the list such that its sum with another integer in the list equals 0.
        :rtype: int
        """
        # sort the input list
        nums.sort()
        # initialize two pointers, i and j, at the beginning and end of the list respectively
        i, j = 0, len(nums) - 1
        # iterate until pointers meet
        while i < j:
            # if the sum of elements at pointers equals 0, return the element at pointer j
            if nums[i] + nums[j] == 0:
                return nums[j]
            # if the sum is less than 0, move pointer i to the right
            elif nums[i] + nums[j] < 0:
                i += 1
            # if the sum is greater than 0, move pointer j to the left
            else:
                j -= 1
        # if no such element is found, return -1
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.findMaxK([-1,2,-3,3]))
    print(s.findMaxK([-1,10,6,7,-7,1]))
    print(s.findMaxK([-10,8,6,7,-2,-3]))