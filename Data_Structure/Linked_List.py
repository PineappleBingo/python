class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# class Solution:
    def printNode1(self, node):
        while 1:
            # print node in single line
            print(node.data, end=" ")
            if node.next == None:
                break
            node = node.next

    def printNode2(self):
            temp = self.head
            # Print contents of LinkedList form Head   
            while temp:
                print(temp.data)
                temp = temp.next
        

list = LinkedList()
first = list.head = node(1)
second = node(2)
third = node(3)

first.next = second
second.next = third


list.printNode1(list.head)
print("\n------")
list.printNode2()



