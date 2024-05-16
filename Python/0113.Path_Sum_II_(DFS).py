from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # base case: if the root is None, return an empty list
        if not root:
            return root
        # initialize a list to store all paths
        all_paths = []
        
        def dfs(node, path):
            # if the current node has a left child, explore it
            if node.left:
                # recursively call dfs with the left child and update the current path
                dfs(node.left, path + [node.left.val])
             # if the current node has a right child, explore it
            if node.right:
                # recursively call dfs with the right child and update the current path
                dfs(node.right, path + [node.right.val])
            # if the current node is a leaf node (no left or right child)
            else:
                # check if the sum of the current path equals the targetSum    
                if sum(path) == targetSum and not node.left and not node.right:
                    # if yes, add the current path to the list of all_paths
                    all_paths.append(path)
        
        # start the depth-first search from the root node with the initial path containing only the root value
        dfs(root, [root.val])
        # return all the paths that satisfy the condition
        return all_paths

if __name__ == '__main__':
    s = Solution()
    print(s.pathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))), 22))
    print(s.pathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))
    print(s.pathSum(TreeNode(1, TreeNode(2)), 0))