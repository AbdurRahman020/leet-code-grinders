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
    def mergeTwoLists(self, list1: Optional[ListNode], list2:
                      Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        pos = head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                pos.next = list1
                list1 = list1.next
            else:
                pos.next = list2
                list2 = list2.next

            pos = pos.next

        if list1 is not None:
            pos.next = list1
        if list2 is not None:
            pos.next = list2

        return head.next


if __name__ == '__main__':
    s = Solution()

    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    print(s.mergeTwoLists(l1, l2).to_list())
    print(s.mergeTwoLists(ListNode(), ListNode(-3)).to_list())
    print(s.mergeTwoLists(ListNode(2), ListNode()).to_list())
