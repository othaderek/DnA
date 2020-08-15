import pdb

class Node:

    def __init__(self, next=None, value=0):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None, tail=None, size=0):
        self.head = head
        self.size = size
        
    def push(self, new_data): 
        # create a new node
        new_node = Node(value=new_data) 
        # set the new nodes value to being the current head
        new_node.next = self.head 
        # set the head to be the new node
        self.head = new_node 
        
    def print_list(self): 
        temp = self.head 
        while temp: 
            print(temp.value) 
            temp = temp.next

    def reverse(self):
        prev = None
        current_node = self.head

        while current_node:
            temp = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = temp
        
        # IMPORTANT: SET HEAD TO PREVIOUS AT END OF LOOP 
        self.head = prev

l1 = LinkedList()
l1.push(3)
l1.push(2)
l1.push(1)
l1.print_list()

pdb.set_trace()

            