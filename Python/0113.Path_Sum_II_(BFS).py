from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # list to store all paths that sum up to the target
        all_paths = []
        
        # check if the root is None
        if not root:
            return all_paths
        
        # initialize a queue for level-order traversal, each element contains (node, remaining sum, current path)
        queue = deque()
        queue.append((root, targetSum, []))
        
        # iterate through the queue until it's empty
        while queue:
            # dequeue the current node, remaining sum, and current path
            node, remaining_sum, curr_path = queue.popleft()
            
            # update the remaining sum by subtracting the value of the current node
            remaining_sum -= node.val
            # append the value of the current node to the current path
            curr_path.append(node.val)
            
            # check if the current node is a leaf node and if the remaining sum equals 0
            if not node.left and not node.right and remaining_sum == 0:
                # if yes, add the current path to the list of all paths
                all_paths.append(curr_path)
            
            # enqueue the left child if it exists, with the updated remaining sum and current path
            if node.left:
                queue.append((node.left, remaining_sum, curr_path[:]))
            # enqueue the right child if it exists, with the updated remaining sum and current path
            if node.right:
                queue.append((node.right, remaining_sum, curr_path[:]))
        
        # return the list of all paths
        return all_paths

if __name__ == '__main__':
    s = Solution()
    print(s.pathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))), 22))
    print(s.pathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))
    print(s.pathSum(TreeNode(1, TreeNode(2)), 0))