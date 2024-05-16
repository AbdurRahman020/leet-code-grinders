from typing import Optional
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        # if the root is None (empty), return 0 (no path possible)
        if not root:
            return count
        
        # initialize a queue for BFS traversal
        queue = deque()
        # start bfs with the root node and its path till that node
        queue.append((root, [root.val]))
        
        # initialize a defaultdict to store the count of path sums encountered so far
        path_sums = defaultdict(int)
        # initialize with 0 sum for paths starting from the root
        path_sums[0] = 1
        
        # perform bfs traversal
        while queue:
            # extract the current node and the path till that node
            node, path_till_node = queue.popleft()
            # calculate the current path sum
            curr_path_sum = sum(path_till_node)
            # increment count if there exist any paths with sum equal 
            # to (current sum - targetSum)
            count += path_sums[curr_path_sum - targetSum]
            # update path_sums dictionary with the current path sum
            path_sums[curr_path_sum] += 1
            
            # add child nodes to the queue along with their paths
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
