'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # traverse each linked list
        l1_list = []
        l2_list = []

        current_node_l1 = l1
        current_node_l2 = l2

        while current_node_l1 != None:
            l1_list.append(current_node_l1.val)
            current_node_l1 = current_node_l1.next

        while current_node_l2 != None:
            l2_list.append(current_node_l2.val)
            current_node_l2 = current_node_l2.next

        l1_list = [str(i) for i in l1_list[::-1]]
        l2_list = [str(i) for i in l2_list[::-1]]
        sum_to_turn_to_ll = int("".join(l1_list)) + int("".join(l2_list))
        
        print(sum_to_turn_to_ll)
        char_list = list(str(sum_to_turn_to_ll))
        print(char_list)
        num_list = [int(char) for char in char_list[::-1]]

        ll_node = ListNode(val=0)
        current_node = ll_node
        for i in num_list:
            current_node.val = i
            current_node.next = ListNode(val=0)
            current_node = current_node.next
        
        current_node = ll_node
        while current_node != None:
            if current_node.next.next == None:
                current_node.next = None
                return ll_node
            current_node = current_node.next

        return ll_node


l1 = ListNode(val=0)
l2 = ListNode(val=1)
l3 = ListNode(val=2)
l1.next = l2
l2.next = l3

m1 = ListNode(val=0)
m2 = ListNode(val=1)
m3 = ListNode(val=2)
m1.next = m2
m2.next = m3


s1 = Solution()

print(s1.addTwoNumbers(l1, m1))

# save each linked list node value to seperate arrays
# turn the list into char list
# join each list as strings
# convert to integers
# sum
# convert to string again, then to list
# create new Linked List with array