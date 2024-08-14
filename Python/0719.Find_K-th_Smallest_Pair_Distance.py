from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Helper function to count how many pairs have a distance <= max_dist
        def count_pairs(max_dist):
            # initialize count of valid pairs and the start index for the sliding window
            count, start = 0, 0

            # iterate over each element in the sorted array using the end pointer
            for end in range(len(nums)):
                # adjust the start pointer to ensure the distance between nums[end] and nums[start] does 
                # not exceed max_dist
                while nums[end] - nums[start] > max_dist:
                    start += 1
                
                # count all pairs with the end element as the second element and any valid start element
                count += end - start
            
            # return the total count of pairs where the distance is <= max_dist
            return count
        
        # sort the array to facilitate the sliding window technique
        nums.sort()
        # initialize binary search boundaries
        min_dist, max_dist = 0, nums[-1] - nums[0]

        # perform binary search to find the smallest distance that allows at least k pairs
        while min_dist < max_dist:
            # compute the middle distance
            mid_dist = (min_dist + max_dist) // 2
            # use count_pairs to determine how many pairs have a distance <= mid_dist
            if count_pairs(mid_dist) < k:
                # if there are fewer than k pairs, mid_dist is too small; increase min_dist
                min_dist = mid_dist + 1
            else:
                # if there are at least k pairs, try smaller distances by adjusting max_dist
                max_dist = mid_dist
        
        # min_dist is the smallest distance where there are at least k pairs
        return min_dist

if __name__ == '__main__':
    s = Solution()
    print(s.smallestDistancePair([1,3,1], 1))
    print(s.smallestDistancePair([1,1,1], 2))
    print(s.smallestDistancePair([1,6,1], 3))