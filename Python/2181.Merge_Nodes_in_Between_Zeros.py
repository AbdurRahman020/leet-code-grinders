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
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize two pointers: slow and fast starting from the head
        slow, fast = head, head.next
        # initialize a variable to accumulate the sum of values encountered
        cumulative_sum = 0
        
        # traverse the list using the fast pointer
        while fast:
            # check if the current node value (fast.val) is 0
            if fast.val == 0:
                # move slow pointer to next node
                slow = slow.next
                # set the value of slow node to cumulative sum
                slow.val = cumulative_sum
                # reset cumulative sum for the next segment of non-zero values
                cumulative_sum = 0
            else:
                # accumulate non-zero values to cumulative sum
                cumulative_sum += fast.val
            
            # move fast pointer to the next node
            fast = fast.next
        
        # after traversal, cut off the list from the last zero node onwards
        slow.next = None
        
        # return the modified head, skipping the initial zero node
        return head.next

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
    print(s.mergeNodes(l1).to_list())
    l2 = ListNode(0, ListNode(1, ListNode(0, ListNode(3, ListNode(0, ListNode(2, ListNode(2, ListNode(0))))))))
    print(s.mergeNodes(l2).to_list())