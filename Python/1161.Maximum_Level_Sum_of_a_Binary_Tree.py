from collections import deque, defaultdict
from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum1(self, root: Optional[TreeNode]) -> int:
        # check if the root is None
        if not root:
            return 0
        
        # initialize with negative infinity to ensure any sum is greater
        max_sum = float('-inf')
        # starting level
        curr_level = 1
        # initialize the level with maximum sum
        max_level  = 0
        
        # initialize a deque with the root node
        queue = deque([root])
        # iterate while the queue is not empty
        while queue:
            # initialize the sum for the current level
            curr_level_sum = 0
            # get the number of nodes at the current level
            n = len(queue)
            
            # iterate over all nodes at the current level
            for _ in range(n):
                # pop the node from the left end of the queue
                curr_node = queue.popleft()
                # add the value of the current node to the sum of the current level
                curr_level_sum += curr_node.val
                
                # add the left child of the current node to the queue if it exists
                if curr_node.left:
                    queue.append(curr_node.left)
                 # add the right child of the current node to the queue if it exists
                if curr_node.right:
                    queue.append(curr_node.right)
            
            # check if the sum of the current level is greater than the maximum sum seen so far
            if curr_level_sum > max_sum:
                # if yes, update the maximum sum and the corresponding level
                max_sum, max_level = curr_level_sum, curr_level
            
            # move to the next level
            curr_level += 1
        
        # return the level with the maximum sum
        return max_level
    
    def maxLevelSum2(self, root: Optional[TreeNode]) -> int:
        # dictionary to store the sum of node values for each level
        level_sum = defaultdict(int)
        
        # function to perform dfs traversal and calculate level-wise sum
        def dfs(node, level):
            # add the value of the current node to the sum of its corresponding level
            level_sum[level] += node.val
            # recursively traverse the left subtree, incrementing the level by 1
            if node.left:
                dfs(node.left, level+1)
            # recursively traverse the right subtree, incrementing the level by 1
            if node.right:
                dfs(node.right, level+1)
        
        # start the DFS traversal from the root node at level 1
        dfs(root, 1)
        # find the maximum sum among all levels
        max_sum = max(level_sum.values())
        # find the level corresponding to the maximum sum
        max_level = min(level for level, total in level_sum.items() if total == max_sum)
        
        # return the level with the maximum sum
        return max_level

if __name__ == '__main__':
    s = Solution()
    
    print(s.maxLevelSum1(TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))))
    print(s.maxLevelSum1(TreeNode(989, None, TreeNode(10250, TreeNode(98693), TreeNode(-89388, TreeNode(-32127))))))
    
    print(s.maxLevelSum2(TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))))
    print(s.maxLevelSum2(TreeNode(989, None, TreeNode(10250, TreeNode(98693), TreeNode(-89388, TreeNode(-32127))))))
