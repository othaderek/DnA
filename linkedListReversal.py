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
        # First set nextnode to the next_node of current
        nextnode = current.next_node
        # the the current nodes next node to equal previous
        current.next_node = previous
        # set previous to equal current
        previous = current
        # set current to equal nextnode
        current = nextnode

    return previous





n1 = Node(1)
n2 = Node(2)

n1.next_node=n2

print(reverse(n1))
# pdb.set_trace()
