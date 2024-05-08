import heapq

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        # get the length of the score list
        n = len(score)
        # create a heap to store scores along with their indices
        heap = []
        for i, s in enumerate(score):
            heapq.heappush(heap, (s, i))
        
        # initialize a list to store ranks
        rank = [''] * n
        # define the medal names
        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        
        # iterate over the heap to assign ranks
        for place in range(n, 0, -1):
            # pop the score with its index from the heap
            s, i = heapq.heappop(heap)
            # assign medals for top 3 scores, otherwise assign rank number
            if place <= 3:
                rank[i] = medals[place - 1]
            else:
                rank[i] = str(place)
        return rank
    
if __name__ == '__main__':
    s = Solution()
    print(s.findRelativeRanks([5,4,3,2,1]))
    print(s.findRelativeRanks([10,3,8,9,4]))