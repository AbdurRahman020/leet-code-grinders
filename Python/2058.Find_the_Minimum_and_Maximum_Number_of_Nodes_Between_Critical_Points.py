import math
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next:
            # if less than 2 nodes, return [-1, -1]
            return [-1, -1]
        
        # initialize pointers to traverse the list
        prev, curr = head, head.next
        # initialize a variable to track the position of nodes
        position = 0
        # initialize variables for first and previous critical point positions
        first_position, prev_position = None, None
        # initialize minimum distance between critical points to infinity
        min_distance = math.inf 

        while curr.next:  # traverse the list until the second last node
            position += 1  # increment the position counter

            # check if the current node is a "critical point" (local extremum)
            if (prev.val > curr.val < curr.next.val) or (
                prev.val < curr.val > curr.next.val
            ):
                # if a previous critical point exists
                if prev_position is not None:
                    # calculate and update the minimum distance between critical points
                    min_distance = min(min_distance, position - prev_position)
                    # update the previous critical point position
                    prev_position = position
                else:
                    # first critical point found, initialize positions
                    first_position = prev_position = position
            
            # move to the next pair of nodes
            prev, curr = curr, curr.next

        if min_distance == math.inf:
            # if no valid critical points found, return [-1, -1]
            return [-1, -1]  

        # return the minimum distance between critical points and the distance between the first and last critical points
        return [min_distance, prev_position - first_position]

if __name__ == '__main__':
    s = Solution()
    print(s.nodesBetweenCriticalPoints(ListNode(1, ListNode(3))))
    l2 = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
    print(s.nodesBetweenCriticalPoints(l2))
    l3 = ListNode(1, ListNode(3, ListNode(2, ListNode(2, ListNode(3, ListNode(2, ListNode(2, ListNode(2, ListNode(7)))))))))
    print(s.nodesBetweenCriticalPoints(l3))