from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Sort workers based on their wage to quality ratio
        workers = sorted([(w/q, q) for w, q in zip(wage, quality)])
        # initialize a heap to keep track of the k smallest quality values
        max_heap = []
        # initialize variables to keep track of the total quality sum and the maximum wage to quality ratio
        quality_sum, max_ratio = 0, 0.0
        
        # iterate through the first k workers
        for i in range(k):
            # update the maximum ratio
            max_ratio = max(max_ratio, workers[i][0])
            # add the current worker's quality to the sum
            quality_sum += workers[i][1]
            # push negative quality values onto the heap to simulate a max heap
            heapq.heappush(max_heap, -workers[i][1])
        
        # calculate the initial result by multiplying the maximum ratio by the total quality sum
        result = max_ratio * quality_sum
        
        # iterate through the remaining workers
        for i in range(k, len(quality)):
            # update the maximum ratio
            max_ratio = max(max_ratio, workers[i][0])
            # add the current worker's quality and remove the lowest quality from the heap
            quality_sum += workers[i][1] + heapq.heappop(max_heap)
            # push the current worker's quality onto the heap
            heapq.heappush(max_heap, -workers[i][1])
            # update the result with the minimum cost so far
            result = min(result, max_ratio * quality_sum)
        
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.mincostToHireWorkers([10,20,5], [70,50,30], 2))
    print(s.mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3))