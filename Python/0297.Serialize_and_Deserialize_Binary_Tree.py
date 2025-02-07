from typing import Optional
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize1(self, root: Optional[TreeNode]) -> str:
        # initialize an empty list to store serialized nodes
        result = []
        # initialize a deque with the root node
        queue = deque([root])
        
        # perform level-order traversal
        while queue:
            # pop the leftmost node from the deque
            node = queue.popleft()
            if node:
                # if the node exists, append its value to the result list
                result.append(str(node.val))
                # enqueue its left and right children
                queue.append(node.left)
                queue.append(node.right)
            else:
                # if the node doesn't exist, append an empty string to signify absence
                result.append('')
        
        # join the elements of the result list with commas and return as a string
        return ','.join(result)
    
    def serialize2(self, root: Optional[TreeNode]) -> str:
        # initialize an empty list to store serialized node values
        result = []
        
        # define a Depth-First Search (DFS) function to serialize the tree
        def dfs(root):
            # if the current node is None
            if not root:
                # append 'None' to represent an empty node
                result.append('None')
                return
            
            # append the string representation of the node's value
            result.append(str(root.val))
            # recursively serialize the left and right subtrees
            dfs(root.left)
            dfs(root.right)
        
        # start the DFS serialization process
        dfs(root)
        
        # join the serialized node values with commas and return the result as a string
        return ','.join(result)

    def deserialize1(self, data: str) -> TreeNode:
        if not data:
            return
        
        # split the serialized data by commas into a list
        lst = data.split(',')
        # create a TreeNode object with the value of the first element in the list
        _root = TreeNode(lst[0])
        # initialize a deque with the root node
        queue = deque([_root])
        
        # iterate through the list starting from index 1
        i = 1
        while queue:
            # pop the leftmost node from the deque
            _node = queue.popleft()
            # if there are more elements in the list and the current element is not empty
            if i < len(lst) and lst[i]:
                # create a left child TreeNode object with the value of the current element
                _node.left = TreeNode(int(lst[i]))
                # enqueue the left child
                queue.append(_node.left)
            
            # increment the index
            i += 1
            # if there are more elements in the list and the current element is not empty
            if i < len(lst) and lst[i]:
                # create a right child TreeNode object with the value of the current element
                _node.right = TreeNode(int(lst[i]))
                # enqueue the right child
                queue.append(_node.right)
            # increment the index
            i += 1
        
        # return the root of the deserialized tree
        return _root
    
    def deserialize2(self, data: str) -> TreeNode:
        # split the serialized string by commas to get a list of node values
        lst = data.split(',')
        self.index = 0
        
        # define a DFS function to deserialize the tree
        def dfs():
            # if the current value is 'None'
            if lst[self.index] == 'None':
                # move to the next index
                self.index += 1
                # return None to represent an empty node
                return None
            
            # create a new TreeNode with the integer value of the current string
            _root = TreeNode(int(lst[self.index]))
            # move to the next index
            self.index += 1
            # recursively deserialize the left and right subtrees
            _root.left = dfs()
            _root.right = dfs()
            
            # return the current node
            return _root
        
        # start the DFS deserialization process and return the root of the deserialized tree
        return dfs()

if __name__ == '__main__':
    c = Codec()
    
    r1 = TreeNode(1)
    r1.left = TreeNode(2)
    r1.right = TreeNode(3)
    r1.right.left = TreeNode(4)
    r1.right.right = TreeNode(5)
    print(c.deserialize1(c.serialize1(r1)))
    
    r2 = TreeNode(None)
    print(c.deserialize1(c.serialize1(r2)))
    
    r3 = TreeNode(5)
    r3.left = TreeNode(4)
    r3.right = TreeNode(3)
    r3.right.left = TreeNode(2)
    r3.right.right = TreeNode(1)
    print(c.deserialize1(c.serialize1(r3)))
