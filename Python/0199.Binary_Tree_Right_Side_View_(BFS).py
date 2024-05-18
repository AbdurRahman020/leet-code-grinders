from typing import Optional, List
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        
        # initialize level size for each level
        queue = deque()
        queue.append(root) 
        
        # traverse all nodes in the current level
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                
                # if it's the last node in the current level, add it to the result
                if i == n - 1:
                    result.append(node.val)
                
                # add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))
    print(s.rightSideView(TreeNode(1, None, TreeNode(3))))
    print(s.rightSideView(None))