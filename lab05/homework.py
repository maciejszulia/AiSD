from BinaryNode import BinaryNode
from BinaryTree import BinaryTree
from typing import Any, Callable, List


# def left_line(tree: BinaryTree) -> List[BinaryNode]:
#     output = []
#     output.append(tree.root)
#     if tree.root.left_child:
#         output.append(tree.root.left_child)
#         tree.traverse_pre_order(output.append())
#     return output

def left_line(tree: BinaryTree) -> List[BinaryNode]:
    output = []
    output.append(tree.traverse_pre_order(output.append(BinaryNode))
    return output


tree = BinaryTree(10)
tree.root.add_left_child(1)
print(left_line(tree))

assert tree.root.value == 10
tree.root.add_right_child(2)
assert tree.root.right_child.value == 2
tree.root.right_child.add_right_child(1)
assert tree.root.right_child.is_leaf() is False
tree.root.add_left_child(1)
tree.root.left_child.add_left_child(1)
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True
