class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, key_value):

        if key_value < self.value:
            if self.left is None:
                self.left = TreeNode(key_value)
            else:
                self.left.insert(key_value)
        else:
            if self.right is None:
                self.right = TreeNode(key_value)
            else:
                self.right.insert(key_value)

    def in_order_traversal(self): # value printed when you arrive at the node for the second time
        if self.left:
            self.left.in_order_traversal()
        print(self.value)

        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self): # value printed when you arrive at the node for the first time
        print(self.value)
        if self.left:
            self.left.pre_order_traversal()

        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self): # value printed when you arrive at the node for the last time
        if self.left:
            self.left.post_order_traversal()

        if self.right:
            self.right.post_order_traversal()

        print(self.value)

    def find(self, key):
        if key < self.value:

            if self.left is None:
                return False
            else:
                return self.left.find(key)

        elif key > self.value:

            if self.right is None:
                return False
            else:
                return self.right.find(key)

if __name__ == "__main__":
    trav = TreeNode(10)
    trav.insert(5)
    trav.insert(4)
    trav.insert(2)
    trav.insert(1)
    trav.insert(3)
    trav.insert(22)
    trav.insert(11)
    trav.insert(12)
    trav.insert(13)

    trav.in_order_traversal()
    trav.pre_order_traversal()
    trav.post_order_traversal()