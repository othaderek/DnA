def BinaryTree(r):
    return [r, [], []]

def insert_left(root, new_branch):
    # pop off the first index
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):
    # pop off the second index
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    
def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0]=newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]
