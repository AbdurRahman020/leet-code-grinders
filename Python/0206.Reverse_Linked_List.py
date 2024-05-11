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
    def reverseList(self, head: ListNode) -> ListNode:
        # initialize two pointers, prev_node and curr_node
        # prev_node will initially be None since it's the tail of the reversed list
        # curr_node starts at the head of the original list
        prev_node, curr_node = None, head
        
        # traverse the original list until curr_node becomes None (end of the list)
        while curr_node:
            # store the next node of the current node before modifying it
            next_node = curr_node.next
            # reverse the pointer of curr_node to point to the previous node
            # this effectively reverses the direction of the linked list
            curr_node.next = prev_node
            # move prev_node and curr_node one step forward for the next iteration
            prev_node = curr_node
            curr_node = next_node
        
        # when the loop ends, prev_node will be pointing to the new head of the reversed list
        # so, return prev_node as the head of the reversed list
        return prev_node

if __name__ == '__main__':
    s = Solution()
    print(s.reverseList(ListNode(1, ListNode(2,ListNode(3, ListNode(4, ListNode(5)))))).to_list())
    print(s.reverseList(ListNode(1, ListNode(2))).to_list())
    print((s.reverseList(ListNode())).to_list())