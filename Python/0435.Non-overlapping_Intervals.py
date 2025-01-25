from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # get the number of intervals
        n = len(intervals)
        # sort intervals based on the end time (second element of each interval)
        intervals.sort(key=lambda e: e[1])
        
        # initialize a counter for the number of overlaps removed
        overlaps_removed = 0
        # set the end of the current interval to the end of the first interval
        curr_end = intervals[0][1]
        
        # iterate through the sorted intervals starting from the second one
        for i in range(1, n):
            # if the start of the current interval is greater than or equal to the end
            # of the last non-overlapping interval, it means there is no overlap
            if intervals[i][0] >= curr_end:
                # update the current end to the end of the current interval
                curr_end = intervals[i][1]
            else:
                # if there's an overlap, increment the count of overlaps removed
                overlaps_removed  += 1
        
        # return the total number of overlaps that were removed
        return overlaps_removed

if __name__ == '__main__':
    s = Solution()
    print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(s.eraseOverlapIntervals([[1,2],[2,3]]))