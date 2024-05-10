import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
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

if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallestPrimeFraction([1,2,3,5], 3))
    print(s.kthSmallestPrimeFraction([1,7], 1))