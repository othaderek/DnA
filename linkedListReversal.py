import pdb

class Node(object):

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def __repr__(self):
        return f'Value: {self.value}, Next: {self.next_node}'


def reverse(head):
    current = head
    previous = None
    nextnode = None

    while current:

        nextnode = current.next_node
        current.next_node = previous

        previous = current
        current = nextnode
    return previous





n1 = Node(1)
n2 = Node(2)

n1.next_node=n2

print(reverse(n1))
# pdb.set_trace()
