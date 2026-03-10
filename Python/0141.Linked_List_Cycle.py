from typing import Optional


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

    @staticmethod
    def build_linked_list(values, pos):
        if not values:
            return None

        nodes = [ListNode(v) for v in values]

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]

        if pos != -1:
            nodes[-1].next = nodes[pos]

        return nodes[0]


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.hasCycle(ListNode.build_linked_list([3, 2, 0, -4], 1)))
    print(s.hasCycle(ListNode.build_linked_list([1, 2], 0)))
    print(s.hasCycle(ListNode.build_linked_list([1], -1)))
