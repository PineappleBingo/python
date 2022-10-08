
# Binary Tree Traversal
# 1. By Level -> Breadth-first

# 2. By Delpth -> Depth-first
# 2-1 : Inorder : <left><root><right>
# 2-2 : Preorder : <root><left><right>
# 2-3 : Postorder : <left><right><root>

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