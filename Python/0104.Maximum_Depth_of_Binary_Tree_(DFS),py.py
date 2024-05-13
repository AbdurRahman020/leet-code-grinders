from typing import Optional
 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # base case, if the node is None, return depth 0
            if node is None:
                return 0
            
            # recursively calculate the depth of the left subtree
            left_depth = dfs(node.left)
            # recursively calculate the depth of the right subtree
            right_depth = dfs(node.right)
           
            # the depth of the current node is the maximum depth of its 
            # left and right subtrees plus 1.
            return max(left_depth, right_depth) + 1
        
        # start the depth-first search from the root node and return the result
        return dfs(root)

if __name__ == '__main__':
    s = Solution()
    print(s.maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
    print(s.maxDepth(TreeNode(1, None, TreeNode(2))))