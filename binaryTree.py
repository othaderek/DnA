class BinaryTree(object):
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None
        
    def __repr__(self):
        return f"[key: {self.key}, left: {self.left_child}, right: {self.right_child}]"
 
    # set left child
    def set_left_child(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
    # set right child
    def set_right_child(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
    # get root
    def get_root(self):
        return self.key
    # set root
    def set_root(self, new_node):
        self.key = new_node
    # get left child
    def get_left_child(self):
        return self.left_child
    # get right child
    def get_right_child(self):
        return self.right_child

