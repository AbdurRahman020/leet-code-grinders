from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: 
        # initialize an empty list to store the values of nodes in inorder
        result = []
        
        # helper function to perform inorder traversal
        def Inorder(root: Optional[TreeNode]):
            # check if the current node is not None
            if root != None:
                # recursively traverse the left subtree
                Inorder(root.left)
                # append the value of the current node to the result list
                result.append(root.val)
                # recursively traverse the right subtree
                Inorder(root.right)
        
        # start inorder traversal from the root node
        Inorder(root)
        
        # return the list of values in inorder traversal
        return result 
    
if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(s.inorderTraversal(r1))
    r2 = TreeNode(1)
    print(s.inorderTraversal(r2))
    r3 = None
    print(s.inorderTraversal(r3))