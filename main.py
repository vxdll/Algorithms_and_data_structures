class Node:
    def __init__(self, key, parent=None, color="red", left=None, right=None):
        self.key = key
        self.parent = parent
        self.color = color
        self.left = left
        self.right = right


class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(key=None, color="black")
        self.root = self.NIL_LEAF

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL_LEAF:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL_LEAF:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF

        if self.root == self.NIL_LEAF:
            self.root = new_node
            self.root.color = "black"
            return

        current = self.root
        parent = None
        while current != self.NIL_LEAF:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self.insert_fixup(new_node)

    def insert_fixup(self, node):
        while node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = "black"

    def print_tree(self, node, level=0, prefix="Root: "):
        if node != self.NIL_LEAF:
            print(" " * (level * 4) + prefix + str(node.key) + " " + node.color)
            self.print_tree(node.left, level + 1, "L--- ")
            self.print_tree(node.right, level + 1, "R--- ")


#Запуск
if __name__ == "__main__":
    rb_tree = RedBlackTree()
    keys = [13,8,17,1,11,15,25,6,22,27]
    for key in keys:
        rb_tree.insert(key)

    rb_tree.print_tree(rb_tree.root)