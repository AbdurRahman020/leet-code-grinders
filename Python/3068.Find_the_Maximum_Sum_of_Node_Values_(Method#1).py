from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # counter to track the number of elements where a is greater than b
        count = 0
        # variable to track the minimum absolute difference between a and b
        min_difference = float('inf')
        # variable to store the total sum of elements after choosing maximum values
        total_sum = 0
        
        # iterate through each element in nums
        for num in nums:
            # value of the element
            a = num
            # XOR operation with k to get the alternate value
            b = num^k
            # if a is greater than b, add a to the total sum
            if a > b:
                total_sum += a
            else:
                # if b is greater than or equal to a, add b to the total sum
                total_sum += b
                # increment count as b is chosen over a
                count += 1
            # update min_difference with the minimum absolute difference between a and b
            min_difference = min(min_difference, abs(a-b))
        
        # if the count of elements where b is chosen over a is odd, adjust the total sum
        if count % 2 == 1:
            total_sum -= min_difference
            
        # return the final total sum
        return total_sum

if __name__ == '__main__':
    s = Solution()
    print(s.maximumValueSum([1,2,1], 3, [[0,1],[0,2]]))
    print(s.maximumValueSum([2,3], 7, [[0,1]]))
    print(s.maximumValueSum([7,7,7,7,7,7], 6, [[0,1],[0,2],[0,3],[0,4],[0,5]]))