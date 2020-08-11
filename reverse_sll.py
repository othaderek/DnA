import pdb

class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse_in_place(node):
    stack = []
    current_node = node
    while current_node != None:
        stack.append(current_node)
        current_node = current_node.next
    
    # loop through list
    # pop off the end
    current_node = stack.pop()
    result = current_node
    while len(stack) != 0:
        current_node.next = stack.pop()
        current_node = current_node.next

    return result

l1 = LinkedListNode(value=1)
l2 = LinkedListNode(value=2)
l3 = LinkedListNode(value=3)
l1.next = l2
l2.next = l3

print(reverse_in_place(l1))

# pdb.set_trace()