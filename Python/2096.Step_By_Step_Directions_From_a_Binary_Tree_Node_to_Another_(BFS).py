from typing import Optional
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
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

if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(6), TreeNode(4)))
    print(s.getDirections(r1, 3, 6))
    r2 = TreeNode(2, TreeNode(1))
    print(s.getDirections(r2, 2, 1))