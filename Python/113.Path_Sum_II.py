class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        if not root:
            return root
        
        all_paths = []

        def dfs(node, path):
            if node.left:
                dfs(node.left, path + [node.left.val])
            if node.right:
                dfs(node.right, path + [node.right.val])
            else:
                if sum(path) == targetSum and not node.left and not node.right:
                    all_paths.append(path)
        
        dfs(root, [root.val])
        return all_paths

if __name__ == '__main__':
    s = Solution()
    print(s.pathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))), 22))
    print(s.pathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))
    print(s.pathSum(TreeNode(1, TreeNode(2)), 0))