from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # base case: if the node is empty, return excess coins as 0 
            # and moves required as 0
            if not node:
                return 0, 0
            
            # recursively traverse the left subtree and right subtree
            left, left_moves = dfs(node.left)
            right, right_moves = dfs(node.right)
            
            # calculate the total moves required for the current node
            total_moves = left_moves + right_moves + abs(left) + abs(right)
            
            # calculate the excess coins at the current node after redistributing,
            # (node.val - 1) represents the excess coins after leaving one coin at 
            # the current node
            return node.val - 1 + left + right, total_moves
        
        # call the dfs function starting from the root of the tree
        _ , moves = dfs(root)
        # return the total moves required for the entire tree
        return moves

if __name__ == '__main__':
    s = Solution()
    print(s.distributeCoins(TreeNode(3, TreeNode(0), TreeNode(0))))
    print(s.distributeCoins(TreeNode(0, TreeNode(3), TreeNode(0))))