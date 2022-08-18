class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()
        print(self.data)

    def Insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.Insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.Insert(data)
        else:
            self.data = data


root = Node(10)
root.Insert(6)
root.Insert(14)
root.Insert(3)
root.PrintTree()
