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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # initialize current and head as a dummy node to hold the result
        curr = head = ListNode()
        # initialize carry to store any carry during addition
        carry = 0
        
        # traverse both linked lists simultaneously until either of them or carry is not None
        while l1 or l2 or carry:
            # determine the values to be added by accessing the value of each node
            # if the node is None, set its value to 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # add the values along with the carry from the previous addition
            val = val1 + val2 + carry
            
            # Update carry by dividing the sum by 10 (to get the carry) and update the sum by
            # taking its remainder when divided by 10
            carry = val//10
            val = val%10
            
            # create a new node with the sum value and set it as the next node of curr
            curr.next = ListNode(val)
            # move curr to the next node
            curr = curr.next
            
            # move l1 and l2 to their respective next nodes if they are not None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # return the next node of head, which contains the result
        return head.next

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print(s.addTwoNumbers(l1, l2).to_list())
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    print(s.addTwoNumbers(l1, l2).to_list())