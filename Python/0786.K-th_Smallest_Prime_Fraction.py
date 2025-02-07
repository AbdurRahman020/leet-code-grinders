from typing import List
import heapq, bisect

class Solution:
    def kthSmallestPrimeFraction1(self, arr: List[int], k: int) -> List[int]:
        # get the length of the array
        n = len(arr)
        # create a min-heap to store fractions and their indices
        heap = [(arr[0] / arr[i], 0, i) for i in range(1, n)]
        heapq.heapify(heap)
        
        # iterate until we reach the kth smallest prime fraction
        for _ in range(k-1):
            # pop the smallest fraction from the heap
            smallest, i, j = heapq.heappop(heap)
            # check if there are more fractions to consider
            if i+1 < j:
                # calculate the next fraction and push it to the heap
                heapq.heappush(heap, (arr[i+1] / arr[j], i+1, j))
        
        # return the kth smallest prime fraction
        return [arr[heap[0][1]], arr[heap[0][2]]]
    
    def kthSmallestPrimeFraction2(self, arr: List[int], k: int) -> List[int]:
        # initialize the search space
        left, right, n = 0, 1, len(arr)
        # binary search loop
        while True:
            # calculate the midpoint of the interval
            mid = (left + right) / 2
            # calculate the border points using binary search
            border = [bisect.bisect(arr, arr[i]/mid) for i in range(n)]
            # count the number of fractions smaller than or equal to mid
            curr = sum(n-j for j in border)
            # adjust the search interval based on the count
            if curr > k:
                right = mid
            elif curr < k:
                left = mid
            # if we've found exactly k fractions
            else:
                # return the fraction with the maximum value, as per the problem statement
                return max(
                    [[arr[i], arr[j]] for i, j in enumerate(border) if j < n],
                    key=lambda x: x[0] / x[1],
                )

if __name__ == '__main__':
    s = Solution()
    
    print(s.kthSmallestPrimeFraction1([1,2,3,5], 3))
    print(s.kthSmallestPrimeFraction1([1,7], 1))
    
    print(s.kthSmallestPrimeFraction2([1,2,3,5], 3))
    print(s.kthSmallestPrimeFraction2([1,7], 1))
