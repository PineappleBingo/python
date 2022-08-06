class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# class Solution:
    def printNode(self, node):
        
        while 1:
            # print node in single line
            print(node.data, end=" ")
            if node.next == None:
                break
            node = node.next
        

list = LinkedList()
first = list.head = node(1)
second = node(2)
third = node(3)

first.next = second
second.next = third

list.printNode(list.head)



