from typing import Optional
from collections import deque, defaultdict

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum1(self, root: Optional[TreeNode]) -> int:
        # initialize a deque with the root node
        q = deque([root])
        
        # continue the loop until the deque is empty
        while q:
           # get the current depth by finding the length of the deque
           depth = len(q)
           # initialize depth_sum to store the sum of values at each depth
           depth_sum = 0
           # iterate through all nodes at the current depth
           for _ in range(0, depth):
               # pop the leftmost node from the deque
               node = q.popleft()
               # add the value of the current node to depth_sum
               depth_sum += node.val
               # if the left child of the current node exists, append it to the deque
               if node.left:
                   q.append(node.left)
               # if the right child of the current node exists, append it to the deque
               if node.right:
                   q.append(node.right)
        
        # return the total sum of node values at all depths
        return depth_sum
    
    def deepestLeavesSum2(self, root: Optional[TreeNode]) -> int:
        # initialize a dictionary to store the sum of node values at each depth
        leaves_sum = defaultdict(int)
        
        def dfs(node, depth):
            # if the current node is None, return to exit the current call
            if not node:
                return
            
            # add the value of the current node to the sum at the current depth
            leaves_sum[depth] += node.val
            # recursively call the function for the left child with increased depth
            dfs(node.left, depth + 1)
            # recursively call the function for the right child with increased depth
            dfs(node.right, depth + 1)
        
        # start depth-first search from the root node with depth 0
        dfs(root, 0)
        # find the maximum depth in the leaves_sum dictionary
        max_depth = max(leaves_sum)
        
        # return the sum of node values at the deepest level
        return leaves_sum[max_depth]
        
if __name__ == '__main__':
    s = Solution()
    
    print(s.deepestLeavesSum1(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), 
                                    TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8))))))
    print(s.deepestLeavesSum1(TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), 
                                    TreeNode(7, TreeNode(1), TreeNode(4))), 
                                       TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))))
   
    print(s.deepestLeavesSum2(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), 
                                   TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8))))))
    print(s.deepestLeavesSum(TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), 
                                    TreeNode(7, TreeNode(1), TreeNode(4))), 
                                       TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))))
