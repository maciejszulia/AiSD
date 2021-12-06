from BinaryNode import BinaryNode
from BinaryTree import BinaryTree
from typing import List, Callable, Any
from lab02 import Queue


def left_line(tree: BinaryTree) -> List[BinaryNode]:



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

# tree.traverse_left_line()
# a = tree.traverse_left_line()

# print(tree.left_line())
print(left_line(tree))
