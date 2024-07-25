from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr: List[int]) -> List[int]:
            n = len(arr)
            
            # base case: if the array has only one element, it's already sorted
            if n <= 1:
                return arr
            
            # divide the array into two halves
            mid = n // 2
            
            # recursively sort the left and right halves
            left_arr = merge_sort(arr[:mid])
            right_arr = merge_sort(arr[mid:])
            
            # merge the sorted halves
            return merge(left_arr, right_arr)
        
        def merge(left_arr: List[int], right_arr: List[int]) -> List[int]:
            # initialize an empty list to store merged result
            merged_arr = []
            # initialize pointers for left_arr and right_arr
            i = j = 0
            # lengths of left_arr and right_arr
            m, n = len(left_arr), len(right_arr)
            
            # merge the two sorted arrays into a single sorted array
            while i < m and j < n:
                if left_arr[i] <= right_arr[j]:
                    merged_arr.append(left_arr[i])
                    i += 1
                else:
                    merged_arr.append(right_arr[j])
                    j += 1
            
            # append remaining elements
            merged_arr.extend(left_arr[i:])
            merged_arr.extend(right_arr[j:])
            
            # return the merged and sorted array
            return merged_arr
        
        # call merge_sort function to sort the input nums array
        return merge_sort(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))
    print(s.sortArray([5, 1, 1, 2, 0, 0]))