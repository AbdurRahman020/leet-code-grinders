from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # initialize a list to store the strings formed from leaf nodes
        result = []
        
        # helper function to perform DFS traversal
        def dfs(root: Optional[TreeNode], val: int) -> bool:
            # base case: if the current node is None, return False
            if not root:
                return False
            
            # append the current node's value to the string 'val', convert node value
            # to corresponding character and append it
            val += chr(ord('a') + root.val)
            
            # recursively traverse left and right subtrees
            left = dfs(root.left, val)
            right = dfs(root.right, val)
            
            # if both left and right child nodes are None, we are at a leaf node
            if not left and not right:
                # append the reversed string to the result list
                result.append(val[::-1])
            
            # return True to indicate that this node was processed
            return True
        
        # start DFS traversal from the root with an empty string
        dfs(root, '')
        # sort the result list to find the smallest lexicographical string
        result.sort()
        
        # return the smallest string from the sorted list
        return result[0]

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(25, TreeNode(1, TreeNode(1), TreeNode(3)), TreeNode(3, TreeNode(0), TreeNode(2)))
    print(s.smallestFromLeaf(r1))
    r2 = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))
    print(s.smallestFromLeaf(r2))
    r3 = TreeNode(2, TreeNode(2, None, TreeNode(1, TreeNode())), TreeNode(1, TreeNode()))
    print(s.smallestFromLeaf(r3))