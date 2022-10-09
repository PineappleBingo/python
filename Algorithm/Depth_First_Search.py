from ast import Or


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#  Example.1
#       a
#      / \
#     b   c
#    / \   \
#   d   e   f

root = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
root.left = b
root.right = c
b.left = d
b.right = e
c.right = f

def DepthFirst_Search_Rec(root, target):
    if root == None:
        return []
    if root.data == target:
        return True
    return DepthFirst_Search_Rec(root.left, target) or DepthFirst_Search_Rec(root.right, target)

print("----------------------")
print(DepthFirst_Search_Rec(root, 'j'))
