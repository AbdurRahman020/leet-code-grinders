from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # get the length of the input list
        n = len(nums)
        # sort the list in descending order
        nums = sorted(nums, reverse=True)
        
        # iterate through the list from the start to the third-last element
        for i in range(n-2):
            # get three consecutive numbers from the sorted list
            a, b, c = nums[i], nums[i+1], nums[i+2]
            # check if the current combination forms a valid triangle
            if a < b + c:
                # if yes, return the perimeter of the triangle
                return a+b+c
        
        # if no valid triangle is found, return 0
        return 0

if __name__ == '__main__':
    s = Solution()
    print(s.largestPerimeter([2,1,2]))
    print(s.largestPerimeter([1,2,1,10]))