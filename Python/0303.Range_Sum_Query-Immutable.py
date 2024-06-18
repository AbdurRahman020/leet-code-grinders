from typing import List

class NumArray:
    
    def __init__(self, nums: List[int]):
        # initialize the prefix sum array
        n = len(nums)
        self.prefix_sum = [0] * (n + 1)
        
        # calculate prefix sums
        for i in range(1, n+1):
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i-1]
    
    def sumRange(self, left: int, right: int) -> int:
        # to find sum of elements from index 'left' to 'right' inclusive, use the prefix
        # sum array formula: sum = prefix_sum[right+1] - prefix_sum[left]
        return self.prefix_sum[right+1] - self.prefix_sum[left]

if __name__ == '__main__':
    commands = ["NumArray", "sumRange", "sumRange", "sumRange"]
    inputs = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    
    nums = inputs[0][0]
    
    obj = None
    results = []
    for i in range(len(commands)):
        command = commands[i]
        if command == "NumArray":
            obj = NumArray(nums)
            results.append(None)
        elif command == "sumRange":
            left, right = inputs[i]
            result = obj.sumRange(left, right)
            results.append(result)
    
    print(results)