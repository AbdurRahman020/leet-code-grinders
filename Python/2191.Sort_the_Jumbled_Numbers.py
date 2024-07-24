from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # a function to map a number to its sorted value using given mapping
        def map_to_sorted_value(num):
            # special case for number 0, directly return mapped value
            if num == 0:
                return mapping[0]
            
            mapped_value = 0
            # used to calculate positional values
            power_of_10 = 1
            
            # extract digits from num and map each digit to its mapped value
            while num > 0:
                # get quotient and remainder of num divided by 10
                q, r = divmod(num, 10)
                # map the digit and add to mapped_value
                mapped_value += mapping[r] * power_of_10
                # update num to next quotient
                num = q
                # increase power_of_10 to next positional value (tens, hundreds, ...)
                power_of_10 *= 10
            
            return mapped_value
        
        # create a list to store tuples of (mapped_value, original_index, original_value)
        num_map = []
        for i, num in enumerate(nums):
            num_map.append((map_to_sorted_value(num), i, num))
        
        # sort num_map based on the mapped_values (first element of each tuple)
        num_map.sort()
        
        # extract original values (third element of each tuple) from sorted num_map
        sorted_nums = [num_map[i][2] for i in range(len(nums))]
        
        return sorted_nums

if __name__ == '__main__':
    s = Solution()
    print(s.sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38]))
    print(s.sortJumbled([0,1,2,3,4,5,6,7,8,9], [789,456,123]))