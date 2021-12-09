from BinaryTree import BinaryTree

tree = BinaryTree(10)

assert tree.root.value == 10
tree.root.add_right_child(2)
assert tree.root.right_child.value == 2
tree.root.right_child.add_right_child(1)
assert tree.root.right_child.is_leaf() is False
tree.root.add_left_child(1)
tree.root.left_child.add_left_child(1)
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True
tree.root.left_child.add_right_child(1)
tree.root.right_child.add_left_child(1)

tree.show()


def left_line():
