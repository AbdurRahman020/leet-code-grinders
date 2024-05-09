class Solution(object):
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        # sort the array in ascending order
        arr.sort()
        
        # iterate over the array starting from the second element and ending 
        # at the second-to-last element
        for i in range(1,len(arr)-1):
            # Check if the difference between the next element and the current element
            # is not equal to the difference between the current element and 
            # the previous element
            if arr[i+1] - arr[i] != arr[i] - arr[i-1]:
                # if the differences are not equal, it is not an arithmetic progression
                return False
        # if all the differences are equal, it is an arithmetic progression
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.canMakeArithmeticProgression([3,5,1]))
    print(s.canMakeArithmeticProgression([1,2,4]))