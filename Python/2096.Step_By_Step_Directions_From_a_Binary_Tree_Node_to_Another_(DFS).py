from typing import List, Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # a helper function to perform Depth-First Search (DFS) and track path
        def dfs(node: TreeNode, val: int, path: List[str]) -> bool:
            # base case: if current node matches the target value
            if node.val == val:
                # return True indicating target found
                return True
            
            # recursive cases
            if node.left and dfs(node.left, val, path):
                # append 'L' to path if found in left subtree
                path += "L"
            elif node.right and dfs(node.right, val, path):
                # append 'R' to path if found in right subtree
                path += "R"
            
            # return the current path list
            return path
        
        # initialize empty lists for paths from root to startValue and destValue
        start_path, dest_path = [], []
        # call dfs to find path to startValue
        dfs(root, startValue, start_path)
        # call dfs to find path to destValue
        dfs(root, destValue, dest_path)
        
        # remove common path elements from the end
        while len(start_path) and len(dest_path) and start_path[-1] == dest_path[-1]:
            # remove elements from start_path
            start_path.pop()
            # remove elements from dest_path
            dest_path.pop()
            
        # construct the final path string
        return "".join("U" * len(start_path)) + "".join(reversed(dest_path))

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(6), TreeNode(4)))
    print(s.getDirections(r1, 3, 6))
    r2 = TreeNode(2, TreeNode(1))
    print(s.getDirections(r2, 2, 1))