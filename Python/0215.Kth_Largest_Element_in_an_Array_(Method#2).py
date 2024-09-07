from random import choice

class Solution:
    def findKthLargest(self, nums, k):
        # define the quick_select function to perform the selection
        def quick_select(nums, k):
            # randomly select a pivot element from nums
            pivot = choice(nums)
            # initialize lists to hold elements based on comparison with pivot
            left, mid, right = [], [], []
            
            # partition the nums list into left, mid, and right based on pivot
            for num in nums:
                if num > pivot:
                    # elements greater than pivot go to the left
                    left.append(num)
                elif num < pivot:
                    # elements less than pivot go to the right
                    right.append(num)
                else:
                    # elements equal to pivot go to the middle
                    mid.append(num)
            
            # if k is less than or equal to the number of elements in left, recursively search in left
            if k <= len(left):
                return quick_select(left, k)
            
            # if k is greater than the number of elements in left plus mid, search in right with updated k
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            
            # if k is within the range of mid, the pivot is the k-th largest element
            return pivot
        
        # call the quick_select function with the initial list and k
        return quick_select(nums, k)

if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))