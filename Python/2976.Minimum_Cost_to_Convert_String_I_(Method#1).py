from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # initialize a 26x26 matrix to represent the cost of converting one character to another,
        # use float("inf") to denote initially no path (no direct conversion cost) between characters
        cost_matrix = [[float("inf")] * 26 for _ in range(26)]
        
        # set the cost of converting a character to itself as zero
        for char_index in range(26):
            cost_matrix[char_index][char_index] = 0
        
        # populate the cost matrix with given conversion costs.
        for orig_char, new_char, conversion_cost in zip(original, changed, cost):
            # convert character to its corresponding index (0-25)
            orig_index = ord(orig_char) - ord("a")
            # convert character to its corresponding index (0-25)
            new_index = ord(new_char) - ord("a")
            # update the cost matrix with the minimum cost of conversion from orig_char to new_char
            cost_matrix[orig_index][new_index] = min(cost_matrix[orig_index][new_index], conversion_cost)
        
        # applying the Floyd-Warshall algorithm to find the minimum cost of conversion between all pairs of characters
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    # update cost_matrix[i][j] with the minimum cost found using an intermediate character k
                    cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][k] + cost_matrix[k][j])
        
        # initialize total conversion cost.
        total_conversion_cost = 0
        
        # compute the total conversion cost for converting the source string to the target string
        for src_char, tgt_char in zip(source, target):
            # only compute cost if characters are different
            if src_char != tgt_char:
                conversion_cost = cost_matrix[ord(src_char) - ord("a")][ord(tgt_char) - ord("a")]
                
                # if conversion cost is still infinity, it means conversion is impossible
                if conversion_cost == float("inf"):
                    return -1
                
                # accumulate the total cost
                total_conversion_cost += conversion_cost
            
        # return the total conversion cost
        return total_conversion_cost

if __name__ == '__main__':
    s = Solution()
    print(s.minimumCost("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]))
    print(s.minimumCost("aaaa", "bbbb", ["a","c"], ["c","b"], [1,2]))
    print(s.minimumCost("abcd", "abce", ["a"], ["e"], [10000]))