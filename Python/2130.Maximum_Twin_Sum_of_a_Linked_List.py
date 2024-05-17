from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # initialize the maximum sum variable
        max_val = 0
        # initialize two pointers: slow and fast
        slow = fast = head
        # initialize a stack to store values
        stack = []
        
        # traverse the list to halfway, storing values in the stack
        while fast and fast.next:
            # move fast pointer two steps ahead
            fast = fast.next.next
            # append the value of the current node to the stack
            stack.append(slow.val)
            # move slow pointer one step ahead
            slow = slow.next
        
        # traverse the remaining half of the list
        while slow:
            # calculate the sum of the current node's value and the top value from the stack
            temp_max = slow.val + stack.pop()
            # update the maximum sum if necessary
            if temp_max > max_val:
                max_val = temp_max
            # move to the next node
            slow = slow.next
        
        # return the maximum sum of paired nodes
        return max_val

if __name__ == '__main__':
    s = Solution()
    print(s.pairSum(ListNode(5, ListNode(4, ListNode(2, ListNode(1))))))
    print(s.pairSum(ListNode(4, ListNode(2, ListNode(2, ListNode(3))))))
    print(s.pairSum(ListNode(1, ListNode(10000))))