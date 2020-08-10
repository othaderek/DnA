import pdb
import sys
import faulthandler

sys.setrecursionlimit(10**6)
faulthandler.enable()

# Node class
# value
# prev
# next
class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    # def __repr__(self):
    #     return f"Node: value: {self.value}, prev: {self.prev}, next: {self.next}"

class DoublyLinkedList:
    def __init__(self, head=None, tail=None, size=0):
        self.head = head
        self.tail = tail
        self.size = size

    # def __repr__(self):
    #     return f"Doubly Linked List: head: {self.head}, tail: {self.tail}, size: {self.size}"

    def search(self, node):
        if self.head == None:
            return None
        current_node = self.head
        while current_node:
            if current_node == node:
                return node
            else:
                current_node = current_node.next
        return None
    
    # Increment size by one
    def insert_at_head(self, value):
        new_node = Node(value=value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return self
        current_head = self.head
        current_head.prev = new_node
        new_node.next = current_head
        self.head = new_node
        self.size += 1
        return self

    def insert_at_tail(self, value):
        if self.tail == None:
            return self.insert_at_head(value)

        new_node = Node(value)
        current_tail = self.tail
        current_tail.next = new_node
        new_node.prev = current_tail
        self.tail = new_node
        self.size += 1
        return self
        
    def insert_before(self, value, node):
        result = self.search(node)
        if result == None:
            return "No node matching in Linked List"
        
        if node == self.head:
            return self.insert_at_head(value)

        new_node = Node(value)
        previous = result.prev
        previous.next = new_node
        new_node.prev = previous
        result.prev = new_node
        new_node.next = result
        self.size += 1
        return self

    def insert_after(self, value, node):
        result = self.search(node)
        if result == None:
            return "No node matching in Linked List"
        
        if node == self.tail:
            return self.insert_at_tail(value)

        new_node = Node(value)
        next_node = result.next
        new_node.next = new_node
        next_node.prev = new_node
        result.next = new_node
        new_node.prev = result
        self.size += 1
        return self


    def delete_node(self, node):
        pass

    def reverse(self):
        pass

d1 = DoublyLinkedList()
# Doubly Linked List Class
# head
# tail
# size
# *methods*
# insert at head
# insert at tail
# insert before given node
# insert after given node
# delete given node
# access
# reverse

pdb.set_trace()