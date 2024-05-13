from typing import Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # define dfs function to perform depth-first search (DFS)
        #  node: current node
        #  target_sum: the target sum to reach
        #  curr_sum: the current sum up to the current node
        #  sum_count: a dictionary to store the count of each sum encountered
        def dfs(node, target_sum, curr_sum, sum_count):
            # if the node is None (empty), return 0 (no path possible)
            if not node:
                return 0
            
            # update the current sum by adding the value of the current node
            curr_sum += node.val
            # calculate the difference between the current sum and the target sum,
            # this will help to find the number of paths that sum up to the target sum
            x = curr_sum - target_sum
            # increment the count of the current sum in the sum_count dictionary
            count = sum_count[x]
            sum_count[curr_sum] += 1
            
            # recursively traverse the left and right subtrees and accumulate
            # the counts of paths that sum up to the target sum
            count += dfs(node.left, target_sum, curr_sum, sum_count)
            count += dfs(node.right, target_sum, curr_sum, sum_count)
            
            # decrement the count of the current sum in the sum_count dictionary
            # to backtrack while exploring different paths
            sum_count[curr_sum] -= 1
            return count
        
        # initialize a defaultdict to store the count of each sum encountered
        sum_count = defaultdict(int)
        # initialize the count for sum 0 to 1, indicating the root 
        # itself could be a valid path
        sum_count[0] = 1
        
        # call the helper function dfs with the root node, targetSum, 
        # initial current sum (0), and sum_count dictionary
        return dfs(root, targetSum, 0, sum_count)

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
    print(s.pathSum(r1, 8))
    r2 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    print(s.pathSum(r2, 22))