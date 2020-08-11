# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # traverse linked list
        # append to list
        # join list
        # check is reversed == normal
        current_node = head
        stack = []
        while current_node != None:
            print(current_node.val)
            stack.append(current_node.val)
            current_node = current_node.next
        char_stack = [str(i) for i in stack]
        num_str = "".join(char_stack)

        if num_str == num_str[::-1]:
            return True
        else:
            return False
        # return char_stack


l1 = ListNode(val=0)
l2 = ListNode(val=1)
l3 = ListNode(val=2)

l1.next = l2
l2.next = l3

# l1.next

s1 = Solution()
print(s1.isPalindrome(l1))

