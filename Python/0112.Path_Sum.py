from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr_sum):
            # base case: if the node is None, return False
            if not node:
                return False
            # update current sum by adding the value of the current node
            curr_sum += node.val
            # if the current node is a leaf node, check if the current sum equals the target sum
            if not node.left and not node.right:
                return curr_sum == targetSum
            # recursively call dfs for left and right children
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
        
        # base case: (an empty tree) if root is None, return None
        if not root:
            return None
        # start the depth-first search from the root with initial sum 0
        return dfs(root, 0)

if __name__ == '__main__':
    s = Solution()
    print(s.hasPathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))), 22))
    print(s.hasPathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))
    print(s.hasPathSum(TreeNode(), 0))