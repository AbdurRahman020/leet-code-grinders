from collections import defaultdict
from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # dictionary to store the sum of node values for each level
        level_sum = defaultdict(int)
        
        # function to perform dfs traversal and calculate level-wise sum
        def dfs(node, level):
            # add the value of the current node to the sum of its corresponding level
            level_sum[level] += node.val
            # recursively traverse the left subtree, incrementing the level by 1
            if node.left:
                dfs(node.left, level+1)
            # recursively traverse the right subtree, incrementing the level by 1
            if node.right:
                dfs(node.right, level+1)
        
        # start the DFS traversal from the root node at level 1
        dfs(root, 1)
        # find the maximum sum among all levels
        max_sum = max(level_sum.values())
        # find the level corresponding to the maximum sum
        max_level = min(level for level, total in level_sum.items() if total == max_sum)
        
        # return the level with the maximum sum
        return max_level

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
    print(s.maxLevelSum(r1))
    r2 = TreeNode(989, None, TreeNode(10250, TreeNode(98693), TreeNode(-89388, TreeNode(-32127))))
    print(s.maxLevelSum(r2))