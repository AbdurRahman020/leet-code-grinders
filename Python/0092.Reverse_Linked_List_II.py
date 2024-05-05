class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head
        
        temp = ListNode(next=head)
        prev = temp

        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next

        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return temp.next

if __name__ == '__main__':
    s = Solution()
    print(s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 5))
    print(s.reverseBetween(ListNode(5), 1, 1))