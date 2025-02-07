from typing import Optional, List
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView1(self, root: Optional[TreeNode]) -> List[int]:
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
    
    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
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
    
    print(s.rightSideView1(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))
    print(s.rightSideView1(TreeNode(1, None, TreeNode(3))))
    print(s.rightSideView1(None))
    
    print(s.rightSideView2(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))
    print(s.rightSideView2(TreeNode(1, None, TreeNode(3))))
    print(s.rightSideView2(None))
