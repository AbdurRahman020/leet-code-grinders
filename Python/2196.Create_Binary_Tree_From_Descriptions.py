from typing import List, Optional
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def serialize(self) -> List[int]:
        """Serialize the tree into a list"""
        result = []
        
        if self is None:
            return result
        
        queue = deque([self])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        
        # remove trailing None values
        while result and result[-1] is None:
            result.pop()
        
        return result

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # to map node values to TreeNode objects
        node_map = {}
        # to track all child nodes
        seen_nodes = set()
        
        # process each description
        for parent, child, left in descriptions:
            # create the parent node if it doesn't exist
            if parent not in node_map:
                node_map[parent] = TreeNode(parent)
            # create the child node if it doesn't exist
            if child not in node_map:
                node_map[child] = TreeNode(child)
            
            # assign the child node as left or right child based on 'left' flag
            if left:
                # set left child
                node_map[parent].left = node_map[child]
            else:
                # set right child
                node_map[parent].right = node_map[child]
            
            # keep track of all seen child nodes
            seen_nodes.add(child)
        
        # find the root node (which will not be a child of any other node)
        for parent, _, _ in descriptions:
            if parent  not in seen_nodes:
                # return the first node that isn't a child
                return node_map[parent]

if __name__ == '__main__':
    s = Solution()
    print(s.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]).serialize())
    print(s.createBinaryTree([[1,2,1],[2,3,0],[3,4,1]]).serialize())
    print(s.createBinaryTree([[10,5,1],[10,15,0],[5,3,1],[5,7,0],[15,12,1],[15,18,0]]).serialize())