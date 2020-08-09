import pdb

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, name):
        self.children.append(Node(name))
        return self
    
    def __repr__(self):
        return f"name: {self.name}, children: {self.children}"

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


otha = Node('Otha')
luna = Node('Luna')

otha.add_child('Pablo')
otha.add_child('Luna')

otha.children[1].add_child('Mar')
otha.children[1].add_child('Sol')

pdb.set_trace()