class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode()
        pos = head
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                pos.next = list1
                list1 = list1.next
            else:
                pos.next = list2
                list2 = list2.next
            pos = pos.next

        if list1 != None:
            pos.next = list1
        if list2 != None:
            pos.next = list2
        
        return head.next

if __name__ == '__main__':
    s = Solution()
    
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    print(s.mergeTwoLists(l1, l2))
    print(s.mergeTwoLists(ListNode(), ListNode(0)))
    print(s.mergeTwoLists(ListNode(), ListNode()))    