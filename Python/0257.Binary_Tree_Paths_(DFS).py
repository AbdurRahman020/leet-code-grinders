from typing import Optional, List

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution():
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # if the root is None (empty tree), return an empty list
        if not root:
            return []
        
        # initialize an empty list to store the paths from root to leaf nodes
        paths_list = []
        
        # define a dfs helper function
        def dfs(node, path):
            # check if the current node is not None
            if node:
                # append the current node's value to the path
                path += str(node.val)
                
                # check if the current node is a leaf
                if not node.left and not node.right:
                    # if it's a leaf, add the completed path to the paths_list
                    paths_list.append(path)
                else:
                    # recursively call dfs for the left child, appending '->' to indicate the path continues
                    dfs(node.left, path + '->')
                    # recursively call dfs for the right child, appending '->' to indicate the path continues
                    dfs(node.right, path + '->')
        
        # start dfs with the root node and an empty path
        dfs(root, '')
        
        # return the list of paths from root to leaf nodes
        return paths_list

if __name__ == '__main__':
    s = Solution()
    print(s.binaryTreePaths(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))))
    print(s.binaryTreePaths(TreeNode(1)))
    print(s.binaryTreePaths(None))