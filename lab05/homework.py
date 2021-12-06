from BinaryNode import BinaryNode
from BinaryTree import BinaryTree
from typing import List


def left_line(tree: BinaryTree) -> List[BinaryNode]:
    output = [tree.root]

    node = tree.root
    left_side_level = 0
    while node.left_child:
        output.append(node.left_child)
        node = node.left_child
        left_side_level += 1

    return output


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

tree.show()
print(left_line(tree))
