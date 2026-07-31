from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, lst: List[int]) -> Optional['ListNode']:
        '''Create a linked list from a Python list'''
        if not lst:
            return None

        head = cls(lst[0])
        curr = head
        for val in lst[1:]:
            curr.next = cls(val)
            curr = curr.next
        return head

    def to_list(self) -> List[int]:
        '''Convert linked list to a Python list'''
        result = []
        curr = self
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if the list is empty, has only one node, or no rotation is needed, return the original list
        if not head or not head.next or k == 0:
            return head

        # initialize the length of the list and locate the tail node
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        # reduce the number of rotations using the length of the list
        k = k % n
        
        # if the effective number of rotations is zero, return the original list
        if k == 0:
            return head

        # connect the tail to the head to form a circular linked list
        tail.next = head

        # locate the new tail after rotation
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next

        # set the new head as the node following the new tail
        new_head = new_tail.next
        
        # break the circular linked list to complete the rotation
        new_tail.next = None

        # return the head of the rotated linked list
        return new_head


if __name__ == '__main__':
    s = Solution()

    print((s.rotateRight(ListNode.from_list([1, 2, 3, 4, 5]), 2)).to_list())
    print((s.rotateRight(ListNode.from_list([0, 1, 2]), 4)).to_list())
