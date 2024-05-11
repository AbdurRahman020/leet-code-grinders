import heapq, math

class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
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

if __name__ == '__main__':
    s = Solution()
    print(s.mincostToHireWorkers([10,20,5], [70,50,30], 2))
    print(s.mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3))