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
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the linked list using a stack
        stack = []
        while head:
            stack.append(head)
            head = head.next
        
        # perform doubling operation with carry-over
        carry = 0
        new_head = None
        while stack:
            # pop node from stack
            node = stack.pop()
            # get the value of the node
            value = node.val
            
            # compute the new value after doubling and add carry
            new_val = value * 2 + carry
            # update node value with the last digit of the new value
            node.val = new_val % 10
            # update carry for the next iteration
            carry = new_val // 10
            
            # re-link the node to the new reversed list
            node.next = new_head
            new_head = node
        
        # if there is a remaining carry-over, add a new node
        if carry:
            new_node = ListNode(1)
            new_node.next = new_head
            new_head = new_node

        return new_head

if __name__ == '__main__':
    s = Solution()
    print(s.doubleIt(ListNode(1, ListNode(8, ListNode(9)))).to_list())
    print(s.doubleIt(ListNode(9, ListNode(9, ListNode(9)))).to_list())