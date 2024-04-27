class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # initialize two stacks to store the values of l1 and l2
        stack1, stack2 = [], []
        
        # populate stack1 with values from l1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        # populate stack2 with values from l2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        # initialize current_node to None and carry to 0
        curr_node, carry = None, 0
        
        # iterate through stacks or carry
        while stack1 or stack2 or carry:
            # pop from stack1 if not empty, otherwise default to 0
            val1 = stack1.pop() if stack1 else 0
            # pop from stack2 if not empty, otherwise default to 0
            val2 = stack2.pop() if stack2 else 0
            # calculate sum and carry
            carry, val = divmod(val1 + val2 + carry, 10)
            # create new node with current value and link it to the current_node
            new_node = ListNode(val, curr_node)
            # update current_node to the newly created node
            curr_node = new_node
        
        # the last node assigned in the loop is the head of the result
        return new_node

if __name__ == '__main__':
    s = Solution()
    print(s.addTwoNumbers(ListNode(7, ListNode(2, ListNode(4, ListNode(3)))), ListNode(5, ListNode(6, ListNode(4)))))
    print(s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))
    print(s.addTwoNumbers(ListNode(), ListNode()))