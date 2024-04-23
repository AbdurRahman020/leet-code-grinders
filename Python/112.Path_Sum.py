class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(node, curr_sum):
            if not node:
                return False
            
            curr_sum += node.val
            if not node.left and not node.right:
                return curr_sum == targetSum
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
        
        if not root:
            return None
        
        return dfs(root, 0)

if __name__ == '__main__':
    s = Solution()
    print(s.hasPathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))), 22))
    print(s.hasPathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))
    print(s.hasPathSum(TreeNode(), 0))