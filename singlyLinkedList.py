import pdb

class Node(object):

    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

    def __repr__(self):
        return f'value: {self.value}, next: {self.nextNode}'

class SingleyLinkedList(object):
    
    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

    def add_node(self,object):
        node = Node(value=object)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.nextNode = node
            self.tail = node
        
        self.length+=1
        return self


    

s1 = SingleyLinkedList()

pdb.set_trace()