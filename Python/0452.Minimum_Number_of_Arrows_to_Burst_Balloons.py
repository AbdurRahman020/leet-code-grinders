from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort the balloons by their start positions (first element of each pair)
        points.sort(key=lambda e: e[0])
        
        # start with one arrow to shoot the first balloon
        arrows = 1
        
        # initialize the current end of the overlap with the first balloon's end position
        curr_end = points[0][1]

        # iterate through the remaining balloons starting from the second one
        for balloon in points[1:]:
            # if the current balloon starts after the current end of the overlap
            if balloon[0] > curr_end:
                # we need a new arrow for this balloon
                arrows += 1
                # update the current end to this balloon's end position
                curr_end = balloon[1]
            else:
                # if they overlap, update the current end to the minimum of the current 
                # end and this balloon's end position to maintain the overlap
                curr_end = min(curr_end, balloon[1])
        
        # return the total number of arrows needed
        return arrows

if __name__ == '__main__':
    s = Solution()
    print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
    print(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))