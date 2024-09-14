from heapq import heapify, heappop, heappush

class SmallestInfiniteSet:
    
    def __init__(self):
        # initialize an empty heap and the current number to start from 1
        self.arr = []
        # convert list to a heap (though it's empty at this point)
        heapify(self.arr)
        # the smallest number to be returned next if heap is empty
        self.curr_num = 1  

    def popSmallest(self) -> int:
        if not self.arr:
            # if the heap is empty, return the current smallest number and increment it
            smallest = self.curr_num
            # increment `curr_num` so that the next smallest number is correctly updated
            # for future `popSmallest` calls when the heap is empty
            self.curr_num += 1
            return smallest
        else:
            # otherwise, pop the smallest number from the heap
            curr_min = heappop(self.arr)
            # remove any duplicate smallest numbers in the heap
            while self.arr and curr_min == self.arr[0]:
                heappop(self.arr)
            # return the smallest number that was popped from the heap.
            return curr_min

    def addBack(self, num: int) -> None:
        # add a number back to the heap if it is less than the current smallest number
        if num < self.curr_num:
            # push the number into the heap, maintaining the heap property
            heappush(self.arr, num)

if __name__ == '__main__':
    commands = ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", 
                "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
    inputs = [[], [2], [], [], [], [1], [], [], []]

    obj = None
    results = []
    for i in range(len(commands)):
        command = commands[i]
        if command == "SmallestInfiniteSet":
            obj = SmallestInfiniteSet()
            results.append(None)
        elif command == "addBack":
            num = inputs[i][0]
            obj.addBack(num)
            results.append(None)
        elif command == "popSmallest":
            result = obj.popSmallest()
            results.append(result)

    print(results)