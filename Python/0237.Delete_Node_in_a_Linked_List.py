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
    def deleteNode(self, node: ListNode) -> None:
        # copy the value of the next node to the current node
        node.val = node.next.val
        # change the pointer of the current node to skip the next node
        node.next = node.next.next

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
    s.deleteNode(l1.next)
    print(l1.to_list())
    l2 = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
    s.deleteNode(l2.next.next)
    print(l2.to_list())