class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        # Check if the data already exists
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data) # Keep iterating recursively
            else :
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # Visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit base node:
        elements.append(self.data)

        # Visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):

        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):

        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def search_val(self,val):

        if self.data == val:
            return True


        if val<self.data:
            if self.left:
                return self.left.search_val(val)
            else:
                return False

        if val>self.data:
            if self.right:
                return self.right.search_val(val)
            else:
                return False

    def findmax(self):
        if self.right:
            return self.right.findmax()
        else:
            return self.data


    def findmin(self):
        if self.left:
            return self.left.findmin()
        else:
            return self.data

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val> self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.findmin()
            self.data = min_val
            self.right = self.right.delete(min_val) # Very important

        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17,5,123,54,12,756,32,5,2,7,7,2]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.search_val(1234))
    print(numbers_tree.findmin())
    print(numbers_tree.findmax())
    numbers_tree.delete(213123)
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(5)
    print(numbers_tree.in_order_traversal())