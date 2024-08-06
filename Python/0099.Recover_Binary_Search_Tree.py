from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # initialize an empty list to store nodes in inorder
        result = []
        
        # helper function to perform inorder traversal and collect nodes
        def Inorder(root: Optional[TreeNode]):
            # check if the current node is not None
            if root != None:
                # recursively traverse the left subtree
                Inorder(root.left)
                # append the current node to the result list
                result.append(root)
                # recursively traverse the right subtree
                Inorder(root.right)
        
        # perform inorder traversal on the tree
        Inorder(root)
        
        # sort the collected nodes based on their values
        new_result = sorted(result, key=lambda x: x.val)
        
        # iterate over the nodes to find and fix the misplaced nodes
        for i in range(len(result)):
            # get the original and sorted node
            m, n = result[i], new_result[i]
            # if the nodes are different, it means a swap occurred
            if m != n:
                # swap the values of the two nodes
                m.val, n.val = n.val, m.val
                # exit the loop after fixing the first discrepancy
                break
        
        # return the root of the modified tree
        return root

if __name__ == '__main__':
    # a helper function to get the inorder traversal of a tree as a list
    def inorder_print(root):
        return inorder_print(root.left) + [root.val] + inorder_print(root.right) if root else []
    
    s = Solution()
    tree1 = TreeNode(1, TreeNode(3, None, TreeNode(2)))
    s.recoverTree(tree1)
    print(inorder_print(tree1))
    tree2 = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
    s.recoverTree(tree2)
    print(inorder_print(tree2))