import math


import math
# Binary Tree Traversal
# 1. By Level -> Breadth-first

# 2. By Delpth -> Depth-first
# 2-1 : Inorder : <left><root><right>
# 2-2 : Preorder : <root><left><right>
# 2-3 : Postorder : <left><right><root>

from json.encoder import INFINITY


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # def PrintTree(self):
    #     if self.left:
    #         self.left.PrintTree()
    #     if self.right:
    #         self.right.PrintTree()
    #     print(self.data)

# ???
#     def Insert(self, data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.Insert(data)

#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.Insert(data)
#         else:
#             self.data = data


# root = Node(10)
# root.Insert(6)
# root.Insert(14)
# root.Insert(3)
# root.PrintTree()

def depthFirst_iter(root):
    # FILO
    stack = [ root ]
    result = []
    if len(stack) == 0:
        return []

    while( len(stack) > 0 ):
        current = stack.pop()
        result.append(current.data)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)     

    return result

def depthFirst_recr(root):
    
    if root == None:
        return []
    leftValues = depthFirst_recr(root.left)
    rightValues = depthFirst_recr(root.right)
 
    return [ root.data, *leftValues, *rightValues ]

def breathFirst(root):
    # FIFO
    queue = [ root ]
    result = []

    if len(queue) == 0:
        return []
    
    while len(queue) > 0:
        # removing front of queue
        # visited
        current = queue.pop(0)
        result.append(current.data)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return result

 
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

# ['a', 'b', 'd', 'e', 'c', 'f']
print(depthFirst_iter(root))
print("-------------------")
print(depthFirst_recr(root))
print("-------------------")
# ['a', 'b', 'c', 'd', 'e', 'f']
print(breathFirst(root))


#  Example 2
#      3
#     / \
#    11  3
#   / \   \
#  4  -2   1

root1 = Node(3)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(-2)
f = Node(1)
root1.left = b
root1.right = c
b.left = d
b.right = e
c.right = f

# --------------------------------
# Depth-first preorder Recursive
# Stack / FILO
# --------------------------------
def TreeSum_df_rec(root):
    # base case
    if root == None: return 0
    return root.data + TreeSum_df_rec(root.left) + TreeSum_df_rec(root.right)

# Depth-first preorder Iterative
def TreeSum_df_iter(root):
     # if root is null, return 0
    if root == None: return 0
    stack = [root]
    totalSum = 0

    while( len(stack) > 0):
        current = stack.pop()
        totalSum += current.data
        if current.left: 
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return totalSum

# or

# def TreeSum_df_iter(root):
#      # if root is null, return 0
#     if root == None: return 0
#     stack = [root]
#     totalSum = root.data

#     while( len(stack) > 0):
#         current = stack.pop()
#         if current.left: 
#             stack.append(current.left)
#             totalSum += current.left.data
#         if current.right:
#             stack.append(current.right)
#             totalSum += current.right.data
#     return totalSum

print("-------------------")
print(TreeSum_df_rec(root1))
print("-------------------")
print(TreeSum_df_iter(root1))
print("-------------------")

# Depth-first preorder Iterative
def TreeMin_df_iter(root):

    stack = [root]
    Smallest = INFINITY

    while( len(stack) > 0):
        current = stack.pop()
        if current.data < Smallest:
            Smallest = current.data    
        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)
    
    return Smallest

# --------------------------------
# Depth-first preorder recursive
# --------------------------------
def TreeMin_df_rec1(root):

    if root == None: return INFINITY
    leftSmall = TreeMin_df_rec1(root.left)
    rightSmall = TreeMin_df_rec1(root.right)
    return min(root.data, leftSmall, rightSmall)

# def TreeMin_df_rec2(root):

#     if root == None: return INFINITY
#     leftSmall = TreeMin_df_rec2(root.left)
#     rightSmall = TreeMin_df_rec2(root.right)
#     return min(root.data, leftSmall, rightSmall)


# Breth-first Iterative
def TreeMin_bf(root):
    
    queue = [root]
    Smallest = root.data

    while( len(queue) > 0):
        current = queue.pop(0)
        if current.data < Smallest:
            Smallest = current.data
        if current.left: 
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return Smallest
        
print(TreeMin_bf(root1))
print("-------------------")
print(TreeMin_df_iter(root1))
print("-------------------")
print(TreeMin_df_rec1(root1))
print("-------------------")
# print(TreeMin_df_rec2(root1))
# print("-------------------")

