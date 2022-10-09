import queue


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


def breathFirst_Search(root, snode):
    '''
    Time Complexity : O(n)
    Space Complexity: O(n)
    '''
    isFound = False
    queue = [root]

    while len(queue) > 0:
        current = queue.pop(0)
        if current.data == snode:
            isFound = True
            break
        else:
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    return isFound 

print("---------------------")
print(breathFirst_Search(root, 'j'))