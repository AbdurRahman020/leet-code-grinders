class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        Deletes a node from a singly linked list in place.
       
       :param node: The node to be deleted.
       :type node: ListNode
       :rtype: None
       """
        # copy the value of the next node to the current node
        node.val = node.next.val
        # change the pointer of the current node to skip the next node
        node.next = node.next.next