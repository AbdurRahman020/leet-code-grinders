from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case: if the root is None, return None
        if root is None:
            return None
            
        if key < root.val:
            # if key is smaller than the current node's value, go to the left subtree
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # if key is greater than the current node's value, go to the right subtree
            root.right = self.deleteNode(root.right, key)
        else:
            # if the current node is the node to be deleted
            if not root.left:
                # if the current node has no left child, return its right child
                return root.right
            elif not root.right:
                # if the current node has no right child, return its left child
                return root.left
            else:
                # if the current node has both left and right children, find the 
                # inorder successor (smallest node in the right subtree)
                successor = root.right
                while successor.left:
                    successor = successor.left
                # copy the value of the successor to the current node
                root.val = successor.val
                # delete the successor node
                root.right = self.deleteNode(root.right, successor.val)

        return root

if __name__ == '__main__':
    s = Solution()
    r = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    print(s.deleteNode(r, 3))
    print(s.deleteNode(r, 0))
    print(s.deleteNode(None, 0))