from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes1(self, root: TreeNode) -> int:
        # variable to store the count of "good" nodes
        count_good_nodes = 0
        
        # if the root is None, return 0 as there are no nodes to process
        if not root:
            return count_good_nodes
        
        # using deque as a queue to perform level-order traversal of the binary tree
        queue = deque()
        # initializing the queue with the root node and its value as the maximum encountered so far
        queue.append((root, root.val))
        
        # loop until the queue is empty
        while queue:
            # dequeue the current node and the maximum value encountered so far in the 
            # path to this node
            curr, prev_max = queue.popleft()
            # if the value of the current node is greater than or equal to the maximum
            # encountered so far, then it is a "good" node
            if curr.val >= prev_max:
                count_good_nodes += 1
            
            # update the maximum encountered value for the child nodes
            curr_max = max(curr.val, prev_max)
            
            # if the current node has a left child, enqueue it with the updated maximum value
            if curr.left:
                queue.append((curr.left, curr_max))
            # if the current node has a right child, enqueue it with the updated maximum value
            if curr.right:
                queue.append((curr.right, curr_max))
        
        # return the count of "good" nodes
        return count_good_nodes
    
    def goodNodes2(self, root: TreeNode) -> int:
        def dfs(node, prev_val):
            # base case: if the node is None, return 0
            if not node:
                return 0
            # Check if the value of the current node is greater than or equal 
            # to the previous maximum value
            elif node.val >= prev_val:
                # if yes, increment the count by 1 and recursively traverse the left 
                # and right subtrees
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else:
                # if not, recursively traverse the left and right subtrees with the 
                # same previous maximum value
                return dfs(node.left, prev_val) + dfs(node.right, prev_val)
        
        # start the dfs traversal from the root node with the root node's value as 
        # the initial maximum value
        return dfs(root, root.val)

if __name__ == '__main__':
    s = Solution()
    
    print(s.goodNodes1(TreeNode(3, TreeNode(1, TreeNode(3)),
          TreeNode(4, TreeNode(1), TreeNode(5)))))
    print(s.goodNodes1(TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))))
    
    print(s.goodNodes2(TreeNode(3, TreeNode(1, TreeNode(3)),
          TreeNode(4, TreeNode(1), TreeNode(5)))))
    print(s.goodNodes2(TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))))
