from typing import Optional, List
from collections import deque 

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution():
    def binaryTreePaths1(self, root: Optional[TreeNode]) -> List[str]:
        # if the root is None (empty tree), return an empty list
        if not root:
            return []
        
        # initialize an empty list to store the paths from root to leaf nodes
        paths_list = []
        # initialize a deque with the root node and its value as the starting path
        queue = deque([(root, str(root.val))])
        
        # process nodes in the queue until it's empty
        while queue:
            # dequeue the front node and its path
            curr_node, curr_path = queue.popleft()
            
            # check if the current node is a leaf
            if not curr_node.left and not curr_node.right:
                # if it's a leaf, add the current path to the paths_list
                paths_list += [curr_path]
            
            # if there is a right child, add it to the queue with the updated path
            if curr_node.right:
                queue.append((curr_node.right, curr_path + '->' + str(curr_node.right.val)))
            
            # if there is a left child, add it to the queue with the updated path
            if curr_node.left:
                queue.append((curr_node.left, curr_path + '->' + str(curr_node.left.val)))
        
        # return the list of paths from root to leaf nodes
        return paths_list
    
    def binaryTreePaths2(self, root: Optional[TreeNode]) -> List[str]:
        # if the root is None (empty tree), return an empty list
        if not root:
            return []
        
        # initialize an empty list to store the paths from root to leaf nodes
        paths_list = []
        
        # define a dfs helper function
        def dfs(node, path):
            # check if the current node is not None
            if node:
                # append the current node's value to the path
                path += str(node.val)
                
                # check if the current node is a leaf
                if not node.left and not node.right:
                    # if it's a leaf, add the completed path to the paths_list
                    paths_list.append(path)
                else:
                    # recursively call dfs for the left child, appending '->' to indicate the path continues
                    dfs(node.left, path + '->')
                    # recursively call dfs for the right child, appending '->' to indicate the path continues
                    dfs(node.right, path + '->')
        
        # start dfs with the root node and an empty path
        dfs(root, '')
        
        # return the list of paths from root to leaf nodes
        return paths_list
        
if __name__ == '__main__':
    s = Solution()
    
    print(s.binaryTreePaths1(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))))
    print(s.binaryTreePaths1(TreeNode(1)))
    print(s.binaryTreePaths1(None))
    
    print(s.binaryTreePaths2(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))))
    print(s.binaryTreePaths2(TreeNode(1)))
    print(s.binaryTreePaths2(None))
