from typing import Optional
from collections import deque
 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case, if the node is None, return depth 0
        if root is None:
            return 0
        
        # initialize a deque to store nodes along with their depths
        queue = deque([[root, 1]])
        
        # perform BFS traversal of the tree
        while queue:
            node, depth = queue.popleft()
            # if the node has a left child, append it to the queue with updated depth
            if node.left:
                queue.append([node.left, depth+1])
            # if the node has a right child, append it to the queue with updated depth    
            if node.right:
                queue.append([node.right, depth+1])
        
        # the final value of 'depth' will be the maximum depth of the tree
        return depth

if __name__ == '__main__':
    s = Solution()
    print(s.maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
    print(s.maxDepth(TreeNode(1, None, TreeNode(2))))