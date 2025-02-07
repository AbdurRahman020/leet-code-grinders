from typing import Optional, List
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getDirections1(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # initialize a deque to store pairs of [node, path] starting from the root
        queue = deque([[root, '']])
        # initialize an empty string to store path to startValue
        start_path = ''
        # initialize an empty string to store path to destValue
        dest_path = ''
        
        # perform BFS using deque
        while len(queue) > 0:
            # dequeue the current node and its path
            curr_node = queue.popleft()
            
            # skip if current node is None
            if curr_node[0] is None:
                continue
            
            # check if current node matches startValue
            if curr_node[0].val == startValue:
                # store the path to startValue
                start_path = curr_node[1]
            
            # check if current node matches destValue
            if curr_node[0].val == destValue:
                # store the path to destValue
                dest_path = curr_node[1]
            
            # enqueue left children with updated paths ('L' for left)
            queue.append([curr_node[0].left, curr_node[1] + 'L'])
            # enqueue right children with updated paths ('R' for right)
            queue.append([curr_node[0].right, curr_node[1] + 'R'])
        
        # initialize the index where paths diverge
        matching_index = 0
        # iterate through the minimum length of start_path and dest_path
        for i in range(min(len(start_path), len(dest_path))):
            # check if characters at index i in start_path and dest_path are equal
            if start_path[i] == dest_path[i]:
                # increment matching_index if characters match
                matching_index += 1
            else:
                # break the loop if characters differ (paths diverge)
                break
        
        # construct the final path string
        return (len(start_path) - matching_index) * 'U' + dest_path[matching_index:]
    
    def getDirections2(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # a helper function to perform Depth-First Search (DFS) and track path
        def dfs(node: TreeNode, val: int, path: List[str]) -> bool:
            # base case: if current node matches the target value
            if node.val == val:
                # return True indicating target found
                return True
            
            # recursive cases
            if node.left and dfs(node.left, val, path):
                # append 'L' to path if found in left subtree
                path += "L"
            elif node.right and dfs(node.right, val, path):
                # append 'R' to path if found in right subtree
                path += "R"
            
            # return the current path list
            return path
        
        # initialize empty lists for paths from root to startValue and destValue
        start_path, dest_path = [], []
        # call dfs to find path to startValue
        dfs(root, startValue, start_path)
        # call dfs to find path to destValue
        dfs(root, destValue, dest_path)
        
        # remove common path elements from the end
        while len(start_path) and len(dest_path) and start_path[-1] == dest_path[-1]:
            # remove elements from start_path
            start_path.pop()
            # remove elements from dest_path
            dest_path.pop()
            
        # construct the final path string
        return "".join("U" * len(start_path)) + "".join(reversed(dest_path))

if __name__ == '__main__':
    s = Solution()
    
    print(s.getDirections1(TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(6), TreeNode(4))), 3, 6))
    print(s.getDirections1(TreeNode(2, TreeNode(1)), 2, 1))
    
    print(s.getDirections2(TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(6), TreeNode(4))), 3, 6))
    print(s.getDirections2(TreeNode(2, TreeNode(1)), 2, 1))