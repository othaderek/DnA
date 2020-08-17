import pdb

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size
        
    def push(self, value):
        new_node = Node(value=value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return self
    
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
        previous = None
        current_node = self.head
        
        while current_node:
            next_node = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = next_node
        
        self.head = previous
    
    def remove_head(self):
        self.head = self.head.next
        self.size -= 1
            
    
    def nth_to_the_last(self, n):
        if n <= 0 or n > self.size:
            return False
        
        k = self.size - n
        
        if k == 0:
            return self.remove_head()
        
        current_node = self.head
        previous = None
        while k is not 0:
            k -= 1
            previous = current_node
            current_node = current_node.next
        
        previous.next = current_node.next
        self.size -= 1
        return self.print_list()
    
    def merge(self, l2):
        p = self.head
        q = l2.head
        s = None
        
        if not q:
            return p
        
        if not p:
            return q
        
        if p and q:
            if p.value <= q.value:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
        
        new_head = s
        
        while p and q:
            if p.value <= q.value:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
                
        if not p:
            s.next = q
        
        if not q:
            s.next = p
            
        return new_head

            
# head
# size

# push
# print_list
# search
# reverse
# nth to the last
            
# head
# size

# push
# print_list
# search
# reverse
# nth to the last

l1 = LinkedList()
l2 = LinkedList()

l1.push(4)
l1.push(3)
l1.push(2)
l1.push(1)

l2.push(5)
l2.push(2)
l2.push(1)

# l1.merge(l2)

pdb.set_trace()



