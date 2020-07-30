class SinglyLinkedListNode:

    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

    def __repr__(self):
        return f'value: {self.value}, next: {self.nextNode}'
    

n1 = SinglyLinkedListNode(value=1)
n2 = SinglyLinkedListNode(value=2)
n1.nextNode = n2

print(n1)
