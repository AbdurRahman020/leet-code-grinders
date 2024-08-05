from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # initialize count to keep track of available spots for planting flowers
        count, prev_flower = 0, 0
        
        # iterate through each spot in the flowerbed
        for spot in flowerbed:
            # if the current spot is already planted with a flower (spot == 1)
            if spot == 1:
                # if the previous spot was also planted with a flower, 
                # it means the current spot cannot be used, so decrement count
                if prev_flower == 1:
                    count -= 1
                # update the status of prev_flower to 1
                prev_flower = 1
            # if the current spot is empty (spot == 0)
            else:
                # if the previous spot had a flower, it means this spot is 
                # unavailable for planting, so update prev_flower to 0
                if prev_flower == 1:
                    prev_flower = 0
                # If the previous spot was also empty, it means we found a valid spot
                # for planting, so increment count and update prev_flower to 1
                else:
                    count += 1
                    prev_flower = 1
        
        # check if the total count of available spots is greater than or equal to 
        # the required number of flowers to be planted
        return count >= n

if __name__ == '__main__':
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,1], 1))
    print(s.canPlaceFlowers([1,0,0,0,1], 2))