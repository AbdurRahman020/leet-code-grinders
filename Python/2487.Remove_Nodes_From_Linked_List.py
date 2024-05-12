from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def to_list(self) -> List[int]:
        """Convert the linked list to a Python list"""
        result: List[int] = []
        curr: Optional['ListNode'] = self
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
        
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize current pointer
        curr = head
        # initialize a stack to store nodes
        stack = []
        # traverse the linked list and keep track of nodes in decreasing order
        while curr:
            # remove nodes from the stack whose value is less than the current node
            while stack and stack[-1].val < curr.val:
                stack.pop()
            # append the current node to the stack
            stack.append(curr)
            # move to the next node
            curr = curr.next
        
        # initialize the next node to None
        next_node = None
        # reconstruct the linked list by popping nodes from the stack
        while stack:
            # pop a node from the stack
            curr = stack.pop()
            # set the next pointer of the current node to the next node in the reconstructed list
            curr.next = next_node
            # update the next node to the current node
            next_node = curr
        
        # return the head of the reconstructed linked list
        return curr

if __name__ == '__main__':
    s = Solution()
    print(s.removeNodes(ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))).to_list())
    print(s.removeNodes(ListNode(1, ListNode(1, ListNode(1, ListNode(1))))).to_list())