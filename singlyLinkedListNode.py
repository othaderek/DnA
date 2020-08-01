class Node(object):

    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

    def __repr__(self):
        return f'value: {self.value}, next: {self.nextNode}'
    

n1 = Node(value=1)
n2 = Node(value=2)
n3 = Node(value=3)
n1.nextNode = n2
n2.nextNode = n3

print(n1)
