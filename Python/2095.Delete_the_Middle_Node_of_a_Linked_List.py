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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case: If the list has 0 or 1 element, return None
        if not head.next:
            return head.next
        
        # initialize two pointers: slow and fast
        slow = fast = head
        
        # traverse the list with two pointers, slow and fast
        while fast and fast.next:
            # move fast pointer two steps ahead
            fast = fast.next.next
            # if fast or fast.next is None (i.e., end of the list is reached), 
            # delete the middle node
            if not fast or not fast.next:
                # delete the middle node by skipping it
                slow.next = slow.next.next
            # move slow pointer one step ahead
            else:
                slow = slow.next
        
        # return the modified head
        return head

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
    print(s.deleteMiddle(l1).to_list())
    l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(s.deleteMiddle(l2).to_list())
    l3 = ListNode(2, ListNode(1))
    print(s.deleteMiddle(l3).to_list())