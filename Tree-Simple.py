class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent #Traverses upstream

        return level

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('laptop')
    laptop.add_child(TreeNode('Yoga'))
    laptop.add_child(TreeNode('HP'))
    laptop.add_child(TreeNode('Windows'))

    mobile = TreeNode('Mobile')
    mobile.add_child(TreeNode('iPhone'))
    mobile.add_child(TreeNode('Xiaomi'))
    mobile.add_child(TreeNode('Redme'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('LGTV'))
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('Samsung'))

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__':
    build_product_tree()