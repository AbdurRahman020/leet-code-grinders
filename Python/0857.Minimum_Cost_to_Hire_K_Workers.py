from typing import List
import heapq, math

class Solution:
    def mincostToHireWorkers1(self, quality: List[int], wage: List[int], k: int) -> float:
        # initialize result to positive infinity and quality_sum to 0
        result, quality_sum = math.inf, 0
        # initialize a max heap to store the negative quality values
        max_heap = []
        # sort workers based on their wage to quality ratio
        workers = sorted([(w/q, q) for w, q in zip(wage, quality)])
        
        # iterate through the sorted workers
        for wage_per_quality, q in workers:
            # push negative quality values onto the max heap
            heapq.heappush(max_heap, -q)
            # add the current worker's quality to the total quality sum
            quality_sum += q
            
            # if the size of the heap exceeds k, remove the smallest quality value
            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)
            
            # if the size of the heap equals k, calculate the result
            if len(max_heap) == k:
                result = min(result, quality_sum * wage_per_quality)
        
        return result
    
    def mincostToHireWorkers2(self, quality: List[int], wage: List[int], k: int) -> float:
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
    
    print(s.mincostToHireWorkers1([10,20,5], [70,50,30], 2))
    print(s.mincostToHireWorkers1([3,1,10,10,1], [4,8,2,2,7], 3))
    
    print(s.mincostToHireWorkers2([10,20,5], [70,50,30], 2))
    print(s.mincostToHireWorkers2([3,1,10,10,1], [4,8,2,2,7], 3))
