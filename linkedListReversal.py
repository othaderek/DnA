class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
    
class LinkedList:
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size
    
    def push(self, new_node):
        node = Node(value=new_node)
        temp = self.head
        node.next = temp
        self.head = node
        self.size += 1
        
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            
    def search(self, target_value):
        current_node = self.head
        
        while current_node:
            if current_node.value == target_value:
                return current_node
            current_node = current_node.next
        return False
    
    def reverse(self):
        current_node = self.head
        previous = None
        
        while current_node:
            temp = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = temp
        
        self.head = previous
    def nth_to_the_last(self, n):
        
        if n == 0:
            return False
        
        if n > self.size:
            return False
        
        current_node = self.head
        counter = 0
        
        while current_node:
            counter += 1
            current_node = current_node.next
        
        k = counter-n
        
        if k is 0:
            self.head = self.head.next
            self.si
            return self.print_list()
            
        previous = None
        current_node = self.head
        while k is not 0:
            k -= 1
            previous = current_node
            current_node = current_node.next
        
        previous.next = current_node.next
        sefl.size -= 1
        return self.print_list()
            
    #push
    #print list
    #search
    #reverse
    #remove nth to the last
            