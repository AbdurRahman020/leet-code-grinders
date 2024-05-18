from typing import Optional, List

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, level):
            # base case: if the node is None, return
            if not root:
                return
            
            # if the length of the result list is equal to the current level,
            # it means this level hasn't been visited yet, so append the value 
            # of the node
            if len(result) == level:
                result.append(root.val)
            
            # explore the right subtree first, then the left subtree, 
            # incrementing the level by 1
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)
        
        # initialize an empty list to store the right side view values
        result = []
        # initialize the starting level of the tree
        level = 0
        # call the dfs function to traverse the tree starting from the root
        dfs(root, level)
        
        # return the list containing the right side view values
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))
    print(s.rightSideView(TreeNode(1, None, TreeNode(3))))
    print(s.rightSideView(None))