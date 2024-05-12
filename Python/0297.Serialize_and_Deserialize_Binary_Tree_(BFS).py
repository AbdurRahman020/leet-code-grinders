from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
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

    def deserialize(self, data: str) -> TreeNode:
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

if __name__ == '__main__':
    ser = Codec()
    deser = Codec()
    
    r1 = TreeNode(1)
    r1.left = TreeNode(2)
    r1.right = TreeNode(3)
    r1.right.left = TreeNode(4)
    r1.right.right = TreeNode(5)
    print(deser.deserialize(ser.serialize(r1)))
    
    r2 = TreeNode(None)
    print(deser.deserialize(ser.serialize(r2)))