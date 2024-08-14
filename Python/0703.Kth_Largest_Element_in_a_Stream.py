from typing import List
from heapq import heapify, heappop, heappush

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        # initialize the KthLargest instance with the given `k` and a list of numbers `nums`
        self.k = k  # store the value of `k`, which represents the 'kth' largest element to maintain
        self.min_heap = nums  # initialize the min-heap with the provided list of numbers
        
        # transform the list into a heap in-place.
        heapify(self.min_heap)

        # ensure the heap contains at most `k` elements by removing the smallest elements if necessary
        while len(self.min_heap) > k:
            # remove the smallest element from the heap
            heappop(self.min_heap)

    def add(self, val: int) -> int:
        # add a new value to the heap
        heappush(self.min_heap, val)

        # if the heap exceeds the size of `k`, remove the smallest element
        if len(self.min_heap) > self.k:
            # remove the smallest element from the heap to maintain its size as `k`
            heappop(self.min_heap)
        
        # return the root of the heap, which is the `kth` largest element in the heap
        return self.min_heap[0]

if __name__ == '__main__':
    commands = ["KthLargest", "add", "add", "add", "add", "add"]
    inputs = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    
    obj = None
    results = []

    for i in range(len(commands)):
        command = commands[i]
        if command == "KthLargest":
            k, nums = inputs[i]
            obj = KthLargest(k, nums)
            results.append(None)
        elif command == "add":
            val = inputs[i][0]
            result = obj.add(val)
            results.append(result)
    
    print(results)