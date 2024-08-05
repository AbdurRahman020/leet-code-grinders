from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # a helper function to perform DFS on the tree and calculate the sum of left leaves
        def dfs(root: TreeNode, Left: bool) -> int:
            # base case: if the current node is None, return 0 (no value to add)
            if not root:
                return 0
            
            # if the current node is a leaf node and it is a left leaf, return its value
            if not root.left and not root.right and Left:
                return root.val
            
            # recursively traverse the left subtree, marking the current node as a left node
            # and traverse the right subtree, marking the current node as not a left node
            return dfs(root.left, True) + dfs(root.right, False)
        
        # start the DFS traversal from the root, marking the initial call with Left=False
        return dfs(root, False)

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(s.sumOfLeftLeaves(r1))
    r2 = TreeNode(1)
    print(s.sumOfLeftLeaves(r2))