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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if the list is empty or has only one node, no need to change
        if not head or not head.next:
            return head
        
        # initialize pointers for odd and even nodes
        odd = head
        even_head = even = head.next
        
        # traverse the list until even or even.next becomes None
        while even and even.next:
            # connect odd node to the next odd node
            odd.next = odd.next.next
            # connect even node to the next even node
            even.next = even.next.next
            # move pointers to the next odd and even nodes
            odd = odd.next 
            even = even.next
        
        # connect the last odd node to the head of even nodes
        odd.next = even_head
        
        # return the modified head
        return head

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(s.oddEvenList(l1).to_list())
    l2 = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
    print(s.oddEvenList(l2).to_list())