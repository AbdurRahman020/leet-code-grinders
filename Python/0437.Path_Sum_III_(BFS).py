from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        if not root:
            return count
        
        queue = deque()
        queue.append((root, [root.val]))
        
        while queue:
            n = len(queue)
            for _ in range(n):
                node, path_till_node = queue.popleft()
                curr_path_sum = 0
                for i in reversed(path_till_node):
                    curr_path_sum += i
                    if curr_path_sum == targetSum:
                        count += 1
                
                if node.left:
                    queue.append((node.left, path_till_node + [node.left.val]))
                if node.right:
                    queue.append((node.right, path_till_node + [node.right.val]))
        
        return count

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
    print(s.pathSum(r1, 8))
    r2 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    print(s.pathSum(r2, 22))
    print(s.pathSum(TreeNode(1, TreeNode(-2), TreeNode(-3)), -1))